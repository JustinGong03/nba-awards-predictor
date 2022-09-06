# NBA Awards Predictor: 2022-2023 Season
## Author: Justin Gong

This project takes player data from 2000-2022 in order to predict the NBA player awards for the 2022-2023 season. This is an end-to-end data science project which involves webscraping raw data from multiple sources to deploying finished models. The project employed the following skills: webscraping, data cleaning, visualization, analysis, preprocessing, model building and testing, hyperparameter tuning, and more. 

## Breakdown of Project Contents 

**data**: Contains all the raw webscraped data utilized in the project 

**models**: Finalized models used during the project, trained with 2000-2022 data (All XGBoost regressors) 

**notebooks**:
- **Part 1**: Converting the raw data into structured datasets and creating new features
- **Part 2**: Exploratory Data Analysis
- **Part 3**: Data preprocessing, model training, and model tuning 
- **Part 4**: Model deployment

**Webscraping.py**: Code used to retrieve data from online databases

**Project Summary**: More in-depth summary of process, analysis, and results of the project

The following models were tested:

- Multiple Linear Regression
- LASSO
- Ridge
- Support Vector
- Random Forest
- **Extreme Gradient-Booster Decision Tree (XGBoost)** (Selected model)

## Predictions for the NBA 2022-2023 Season:

### Most Valuable Player

1. ***Joel Embiid*** (0.861 shares)
2. Nikola Jokić (0.771 shares)
3. Giannis Antetokounmpo (0.619 shares)
4. Trae Young (0.191 shares)
5. Stephen Curry (0.150 shares)

### Defensive Player of the Year

1. ***Bam Adebayo*** (0.443 shares)
2. Mikal Bridges (0.390 shares)
3. Rudy Gobert (0.364 shares)
4. Matisse Thybulle (0.197 shares)
5. Chuma Okeke (0.162)

### Sixth Man of the Year

1. ***DeAndre Jordan*** (0.646 shares)
2. Omer Yurtseven (0.639 shares)
3. Kevin Love (0.622 shares)

### Most Improved Player

1. ***Elfrid Payton*** (0.180 shares)
2. Robert Williams (0.163 shares)
3. Mitchell Robinson (0.157 shares)
4. Josh Jackson (0.155 shares)
5. Jarred Vanderbilt (0.154 shares)

### Rookie of the Year

The Rookie of the Year award could not be predicted because I couldn't project 2023 season data without any previous seasons.

## Model Performance for 2021 and 2022 Seasons:

*Note*: 2021 and 2022 were my test sets, however I retrained the model using these two seasons for 2023 season predictions.

### Most Valuable Player

<img width="953" alt="Screen Shot 2022-09-06 at 2 48 21 AM" src="https://user-images.githubusercontent.com/92960950/188566374-037bbc34-ea75-427b-815d-c6a3c42d79d8.png">

### Rookie of the Year

<img width="823" alt="Screen Shot 2022-09-06 at 2 48 55 AM" src="https://user-images.githubusercontent.com/92960950/188566616-2e1c4a4e-588f-4c79-8345-1d352215194d.png">

### Sixth Man of the Year

<img width="830" alt="Screen Shot 2022-09-06 at 2 49 35 AM" src="https://user-images.githubusercontent.com/92960950/188566677-6f68fd82-9146-4a9e-aebd-7ec72460cd79.png">

### Defensive Player of the Year

<img width="949" alt="Screen Shot 2022-09-06 at 2 50 04 AM" src="https://user-images.githubusercontent.com/92960950/188566955-a0c6ebf6-2910-4e4a-b2c3-7bb56a6b6646.png">

### Most Improved Player

<img width="811" alt="Screen Shot 2022-09-06 at 2 50 44 AM" src="https://user-images.githubusercontent.com/92960950/188566986-d6a51116-6f1f-4a18-a032-6a70f2ee7964.png">

## Model Performance for MVP
I ran a backtest with the MVP model to predict each season's MVP since 2006 (Found in part 3). Below were the results:

| Year | Predicted Player | Real Player |
| ---- | ---------------- | ----------- |
| 2006 | Kobe Bryant | Steve Nash |
| 2007 | Steve Nash | Dirk Nowitzski |
| 2008 | LeBron James | Kobe Bryant |
| 2009 | LeBron James | LeBron James |
| 2010 | LeBron James | LeBron James |
| 2011 | Derrick Rose | Derrick Rose |
| 2012 | LeBron James | LeBron James |
| 2013 | LeBron James | LeBron James |
| 2014 | Kevin Durant | Kevin Durant |
| 2015 | Stephen Curry | Stephen Curry |
| 2016 | Stephen Curry | Stephen Curry |
| 2017 | James Harden | Russell Westbrook |
| 2018 | James Harden | James Harden |
| 2019 | Giannis Antetokounmpo | Giannis Antetokounmpo |
| 2020 | Giannis Antetokounmpo | Giannis Antetokounmpo |
| 2021 | Nikola Jokić | Nikola Jokić |
| 2022 | Giannis Antetokounmpo| Nikola Jokić |

## Final Takeaways

In the end, the XGBoost regressor model did a decent job at predicting the awards. However, there were many drawbacks:

1. Voter Fatigue

I had to adjust predictions to account for **voter fatigue** (Concept that votes for players dramatically decrease if they win the award consecutively). For example, my original backtest made *LeBron James* a 6x consecutive MVP. However, I reduced the player voting share by .2 and redistributed it if they won back-to-back, resulting in correctly predicting *Derrick Rose* as the MVP in 2011. 

2. Media Influence 

The media and fan perception of players has a huge influence on award shares. For example, if a player is on a mainstream team and receives praise from the media, they're more likely to win the award because of the attention they receive. However, these models purely looks at the numebrs. For example, Anthony Edwards had better player statistics for ROY in 2021, but LaMelo Ball won it due to his prescense in the media. 

3. Injuries 

Injuries are nearly impossible to predict as any player can get in the NBA season. This heavily impacts awards. For example, Nikola Jokic is predicted to be 2nd in MVP votes in 2023, but this doesn't account for Jamal Murray and Michael Porter Jr. returning for the 2023 season. This would reduce the significance that Jokic would individualy have on his team. 

4. Difficulty in Predicting Shares

The model inherently predicts the voting share relative to *all* the training data. For example, in a given year if every player performs at a high level, then they will receive high voting shares because they performed well compared to players in *previous* seasons. However, in real life, only the *best* player would receive a high voting share because it's scaled relative to the season. Thus, this is a large reason why the shares seen above are substantially inaccurate for many players. 

5. SMOY Qualification

SMOY candidates are players who started less than *half* the games they played. This is difficult to predict for the 2023 NBA season. This process left out major SMOY candidates including Tyler Herro, Jordan Poole, and Terrance Mann as I projected them to start more games next season.

6. Correlation, not Causation

A notorious problem is regression analysis, there are many features that were deemed important because they were correlated with the target variable, but not the cause for it. For example, the defensive player of the year favors *rebounds* and being a *center*/*power forward*. This is because historically big men have won the award, causing their rebound count to be higher. However, rebounds is not relevant to the award. This resulted in the DPOY in 2022, Marcus Smart, to not be predicted because he was the first *guard* to win the award since Gary Payton in 1986 (Not in the model)

What's Next?

Even though this model performed well, it can definitely perform at a higher level. In order to improve prediction power, I can combine classification with regression. Since the majority of NBA players receive 0 award shares for all awards, I can use classification to first predict who will even *receive* a vote. From here, I can then use regression to predict the share. This will improve the distribution of the target variables.

