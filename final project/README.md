<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# FInal Project: Forecasting with Prophet & ARIMA - Doge & Ethereum
*[Ayub Pathan]*

*[Data Analytics, Remote & May 2021]*

## Content
- [Project Description](#project-description)
- [Questions & Hypotheses](#questions-hypotheses)
- [Dataset](#dataset)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
Everyone is going gaga over how the most volatile virtual currencies making people filthy rich over nights if one had invested
in those virtual coins in the past. However, it is not always the case. As word defines, they are extremely volatile and such kind of investement make or break the financial freedom of the investors. However, as part of learning and proejct building, I was interested to check how these decentralized currency behaves over time as well as try to make prediction witht he help of FB Prophet and ARIMA models to make a possible future forecasting though I knew it was not a easy task :).


## Questions & Hypotheses
How crypto currency behaves over time?
What are the major contributors/factors influencing the prices?
Does FB Prophet do can predict the price for a day accurately?
Applying ARIMA Model to generate predictive forecasting model


## Dataset
I have taken recently uploaded cryptocurrencies data from the Kaggle.
Out of several currencies, I have selected only two of them as part of data exploration
and analysis - Dogecoin and Ethereum. 
Each file contains 10 columns and 2159 rows. 


## Workflow: 
Data analysis was done in several steps:

#### Data preprocessing:
Understanding
Finding of nan values if any & their relevancy

#### FB PROPHET:
For Prophet, we have to make new dataframe out of date and required price column. In my case, it was Close (values).
My first approach was to apply FB Prophet to both doge and Ethereum coins at once and see how well this model works. 
So far, it was the most simple model. However, the accuracy was not so convincing from both the currencies. 
Hence as more exploration, I decided to move to ARIMA model.

#### ARIMA:
ARIMA stands for AutoRegression Integrated Moving Average. 
To apply this model, one of the first requirement is the time series should be staionary. 
In my case, after checking, p-values of my data signal, time series was not staionary and hence i had to use 1 log method to 
the signal staionary and take statitics with the help of ADF (Augmented Dickey Füller test). 
Another approach was to do differencing. 

ARIMA(p,d,q):
- ARIMA can be used to forecast the time series with significant dependence among values.
- ARIMA model is characterized by 3 terms: p, d, q where,
    - p is the order of the AR term
    - q is the order of the MA term
    - d is the number of differencing required to make the time series stationary
 
#### Partial Auto Correlation Fuction:
Particla auto correlation function plot gives us required p values.
The Partial Auto Correlation factor(PACF) is the partial correlation between the 
two points at a specific lag of time.

#### Auto Correlation Function:
ACF measures the linear relationships between observations at different time lags.
In other words, ACF is used to understand if there exists a correlation between a 
time series data point with another point as a function of their time difference.

#### Auto-Arima:
It provides best order of p,d,q for ARIMA model if user define start, end values of p & q values 
with other required few parameters. This was the one was used in this project to know if manually achieved
p,d,q ordering was mathing to auto generated or not.


#### Final - Data splitting, model fitting and prediction:
At the end data was splitted based on number of rows. We can not use random selection because this is a time series. 
Two different achieved models were fitted and future forecasting was done. 
 

## Organization
Through the proejct, I used trello board to organise my work

