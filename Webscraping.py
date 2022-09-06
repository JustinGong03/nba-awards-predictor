import pandas as pd 
import numpy as np
import requests as rq 
from bs4 import BeautifulSoup 
from selenium import webdriver 
from itertools import product
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome(ChromeDriverManager().install()) #initializing webdriver for future use

#helper functions
def to_int(games): #used in mutate function
    if(games.isnumeric()):
        return int(games)
    else:
        return 0

def mutate(data): #removes players with less than 41 games played + aggregates player data with multiple teams 
    df = data[data["G"].apply(to_int) > 41].reset_index(drop = True)
    for x in df["Player"].value_counts()[df["Player"].value_counts() > 1].keys():
        temp = df[df["Player"] == x]["Tm"]
        remove = temp[temp != "TOT"].keys()
        df = df.drop(remove).reset_index(drop = True)
    return df

def clean_standings(df): #fixes the formatting of scraped team data
    names = list(df.iloc[0])
    names[0] = "Seed"
    df.columns = names
    df.drop(0, axis = 0, inplace = True)
    df.drop(np.nan, axis = 1, inplace = True)

def get_players(year, category): #returns an array of players for qualified rookies or sixth men in an inputted year
    if category == "R": #rookie data
        url = "https://www.basketball-reference.com/leagues/NBA_{}_rookies-season-stats.html".format(str(year))
        rookies = rq.get(url)
        parse = BeautifulSoup(rookies.text, "html.parser")
        parse.find("tr", class_ = "over_header").decompose()
        data = parse.find_all(id = "rookies")
        df = pd.read_html(str(data))[0]
        return df["Player"]
    
    elif category == "S": #sixth men
        df = pd.read_csv("data/player_data/per_minute_{}".format(str(year)))
        return df[df["GS"] < (df["G"] / 2)].reset_index()["Player"]
    
    elif category == "A": #all-stars
        url = "https://basketball.realgm.com/nba/allstar/game/rosters/{}".format(str(year))
        stars = rq.get(url)
        parse = BeautifulSoup(stars.text, "html.parser")
        data = parse.find_all(class_ = "basketball compact")
        x = pd.read_html(str(data))[0]
        y = pd.read_html(str(data))[1]
        return pd.concat([x, y], axis = 0)["Player"]
    
    else:
        return "Invalid Category"

#scraping voting share data for each award type
def mvp_data():
    agg = pd.DataFrame()
    
    for year in range(2000, 2023):
        url = "https://www.basketball-reference.com/awards/awards_{}.html".format(year)
        mvps = rq.get(url)
        parse = BeautifulSoup(mvps.text, "html.parser")
        parse.find("tr", class_ = "over_header").decompose()
        data = parse.find_all(id = "mvp")
        df = pd.read_html(str(data))[0]
        df["Year"] = year
        
        agg = pd.concat([agg, df[["Player", "Share", "Year"]]], axis = 0)
    agg.to_csv("data/awards_data/mvp_data", index = False)

#note: I am aggregating the datasets in the following 4 award categories for efficiency purposes as selenium is required
#instead of BeautifulSoup

#scraping sixth man of the year award share data 
def award_data():
    agg = pd.DataFrame()
    
    for year, award in product(range(2000, 2023), ["roy", "dpoy", "smoy", "mip"]):
        url = "https://www.basketball-reference.com/awards/awards_{}.html".format(year)
        driver.get(url) 
        driver.execute_script("window.scrollTo(1, 1000)")
        time.sleep(2)
        
        parse = BeautifulSoup(driver.page_source, "html.parser")
        data = parse.find_all(id = award)
        df = pd.read_html(str(data))[0]
        
        df = df.droplevel(0, axis = 1)
        df["Year"] = year
        
        agg = pd.concat([agg, df[["Player", "Share", "Year"]]], axis = 0)
    agg.to_csv("data/awards_data/{}_data".format(award), index = False)
    
#scraping player per 36 data (> 41 games played)
def player_data():
    for year, type_ in product(range(2000, 2023), ["per_minute", "advanced"]):
        driver.get("https://www.basketball-reference.com/leagues/NBA_{}_{}.html".format(year, type_))
        driver.execute_script("window.scrollTo(1, 1000)")
        time.sleep(2)
        html = driver.page_source
        
        parse = BeautifulSoup(html, "html.parser")
        parse.find("tr", class_ = "thead").decompose()
        data = parse.find_all(id = "{}_stats".format(type_))
        df = pd.read_html(str(data))[0]
        
        df = mutate(df)
        df["Year"] = year
        df.to_csv("data/player_data/{}_{}".format(type_, year), index = False)
            
#scraping team data 
def team_data():
    for year in range(2000, 2023):
        data = rq.get("https://www.landofbasketball.com/yearbyyear/{}_{}_standings.htm".format(year-1, year))
        parse = BeautifulSoup(data.text, "html.parser")
        data = parse.find_all(class_ = "color-alt margen-b8 bb")
        east = pd.read_html(str(data))[0]
        west = pd.read_html(str(data))[1]
        
        clean_standings(east)
        clean_standings(west)
        final_df = pd.concat([east, west], axis = 0).reset_index(drop = True)
        final_df.to_csv("data/team_data/{}".format(year), index = False)

def defensive_stats():
    final_df = pd.DataFrame()
    for year in range(1999, 2022):
    #utilizing selenium to find desired data table
    url = "https://www.nba.com/stats/players/defense/?sort=DEF_WS&dir=-1&Season={}-{}&SeasonType=Regular%20Season"
    url = url.format(year, str(year + 1)[-2:])
    driver.get(url)
    time.sleep(5)
    select = Select(driver.find_element("xpath", r"/html/body/main/div/div/div[2]/div/div/nba-stat-table/div[1]/div/div/select"))
    select.select_by_index(0)
    
    #saving data into a dataframe
    parse = BeautifulSoup(driver.page_source, "html.parser")
    data = parse.find_all(class_ = "nba-stat-table__overflow")
    df = pd.read_html(str(data))[0]
    
    #modifying dataset
    df = df[df["GP"] > 41].reset_index(drop = True)
    if df.columns[0] != "Player":
        df = df.iloc[:, 0:21].drop(df.columns[0], axis = 1)
    df["Year"] = year + 1
    df.to_csv("data/player_data/defensive_{}".format(year + 1))

mvp_data()
award_data()
player_data()
team_data()
defensive_stats() 