<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Google Plays Store - Predictive Ranking and Sentiment Analysis
*[Sarah Vonderberg]*

*[DAFT, MAR21, Remote Campus]*

## Content
- [Project Description](#project-description)
- [Hypotheses / Questions](#hypotheses-questions)
- [Dataset](#dataset)
- [Cleaning](#cleaning)
- [Analysis](#analysis), [Model Training and Evaluation](#model-training-and-evaluation), [Sentiment Analysis](#sentiment-analysis)
- [Workflow](#workflow)
- [Conclusion](#conclusion)
- [Organization](#organization)
- [Links](#links)

## Project Description
Out of personal interest for the topic, I chose to work on Apps, specifically on data from the Google Play Store. I wanted to figure out if it is possible to predict app ranking with the data accessible from the Google Play Store as well as if it's possible to see a clear sentiment concerning app reviews.

## Hypotheses / Questions
* Q1: Is it possible to predict app ranking with data from the Google Play Store?
If yes it could be helpful to know which features are important in correlation to "Ranking"
* Q2: Is it possible to see a clear negative/ positive sentiment in terms of app reviews?
If yes, it could help determine good and bad features of an app, as well as problems and issues that users comment on.


## Dataset
> The data for both analyses was retreived publicly from Kaggle.

Predictive Ranking Analysis:
* The original table contained 1118136 rows with 23 columns.
* After data cleaning I was left with a dataset of 1079837 rows and 15 columns, mostly numerical and 2 object types).
* After data preprocessing, I was left with a dataset of 1011976 rows and 42 columns, all numerical.

Review Sentiment Analysis:
* The original table contained 11034 rows with 12 columns.
* The table contained reviews of 15 unique apps.
* For my analysis I chose the app "Microsoft To-Do", as I'm familiar with the app.
* This particular app had review content as follows:
    * 1 Star: 200 rows
    * 2 Star: 200 rows
    * 3 Star: 400 rows
    * 4 Star: 200 rows
    * 5 Star: 200 rows


## Cleaning
For the Ranking Prediction I dropped all NaN values in the features that I need to train the model, as well as columns that I don't need for the prediction (such as AppID, Developer Name etc.).
In order to clean the data I used regular expressions as well as replace functions. In order to convert all app sizes and currencies to one metric, I used functions. I further summed up, some of the values to have balanced features. All columns with dates had to be converted to datetime and then ordinal. I also used these columns to create new data, such as "App-Age". 

Preprocessing:
 I checked for correlation and high collinearity and dropped unnecessary columns. I then checked for outliers via the z-score and dropped those.
 After all data was cleaned, I got dummies for the last 2 object type columns (Category & Content Rating). All boolean type columns were converted to 1s and 0s.
 As the column I wanted to predict was "Ranking", I dropped all Apps with 0 Ranking (not ranked at all), as it would not make sense to train the model with that. 

 For the Review Sentiment Analysis I did not need to clean the data, as it was already clean. I only had to choose the app that I was looking into and filter it for that.

## Analysis
Description is in the [Workflow](#workflow).

## Model Training and Evaluation
Description is in the [Workflow](#workflow).

## Sentiment Analysis
Description is in the [Workflow](#workflow).

## Workflow
Predictive Ranking Analysis:
1. After cleaning and prepocessing the data ([Cleaning](#cleaning)) I used Train Test Split (80/20) to split my dataset.
2. Checking on the "Ranking" uniqe values it was clear that I needed to use regression (values were 1.1, 1.2, 1.3 etc.).
3. I trained different regression models (Linear Regression w. different Scalers (Robust, Standart and Min/Max), Random Forest Regressor, Decision Tree Regressor, KNeighbors Regressor).
4. To increase accuracy I finetuned the best max-depth parameter.
5. For each model I compared the R2, RMSE and Cross Validation Score.
6. As a result, the highest CV Score was 0.1 which is obviously incredible bad and shows that the data is not fit to train prediction models.

Review Sentiment Analysis:
1. After cleaning and prepocessing the data ([Cleaning](#cleaning)) I split the data in 3 sets.
2. Positive reviews (5 & 4 Stars), neutral reviews (3 Stars) and negative reviews (2 & 1 Stars).
3. Then I used "Wordcloud" to generate my figures.
4. I then finetuned my clouds by updating the stopwords.

## Conclusion
* Q1: Is it possible to predict app ranking with data from the Google Play Store?
* A1: No. The features which are accessible by the Google Play Store are not correlated to "Ranking" andtherefore cannot be used to predict app ranking.
It is very likely that features such as Design, Graphics, Sound and Gameplay/Usability are the driving forces in app ranking. These can only be obtained by in-depth user interviews.

* Q2: Is it possible to see a clear negative/ positive sentiment in terms of app reviews?
* A2: Yes, with a review sentiment analysis it is possible to see clear painpoints of users as well as the reasons why an app is loved. This can used to monitor the sentiment of your own app or to figure out issues or great features with competitors.

## Organization
I organised my project with trello into tasks which are either in progress, done or in review. I also assigned deadlines to some tasks in order to be reminded.

I tried to keep my github repo as clean and lean as possible, so it contains:

- a gitignore
- a readme
- a "Code" folder with 3 jupiter notebooks (Data_cleaning-exploration, Model_training_analysis and Review_Sentiment_Analysis )
- a "Figure" folder with all graphs used in my presentation
- (a "Data" folder with the raw as well as cleaned data files -> since they are too big for this repo, find them here: https://github.com/Salevo/Google-app-Store-Analysis)

## Links

[Repository](https://github.com/Salevo/Project-Week-8-Final-Project)  
[Slides](https://drive.google.com/file/d/1-XM7RwOIUfe6E_Ghkd316h5u0wx3uVZ-/view?usp=sharing)  
[Trello](https://trello.com/b/IeR569zR/google-play-store-apps)  
