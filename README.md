# NBA Awards Predictor: 2022-2023 Season
## Author: Justin Gong

This project takes player data from 2000-2022 in order to predict the NBA player awards for the 2022-2023 season. This is an end-to-end data science project which involves webscraping raw data from multiple sources to deploying finished models. The project employed the following skills: webscraping, data cleaning, visualization, analysis, preprocessing, model building and testing, hyperparameter tuning, and more. 

## Breakdown of Project Contents 

**data** 
- Contains all the raw webscraped data utilized in the project 
**models**
- Finalized models used during the project, trained with 2000-2022 data (All XGBoost regressors) 
**notebooks**:
- **Part 1**: Converting the raw data into structured datasets and creating new features
- **Part 2**: Exploratory Data Analysis
- **Part 3**: Data preprocessing, model training, and model tuning 
- **Part 4**: Model deployment
**Webscraping.py**
- Code used to retrieve data from online databases
**Project Summary**
- More in-depth summary of process, analysis, and results of the project

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



