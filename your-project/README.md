<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Rossman - Sales Forecast
*[Faisal Hammad*

*[DAFT-RMT-MAR21]*

## Content
- [Project Description](#project-description)
- [Hypotheses / Questions](#hypotheses-questions)
- [Dataset](#dataset)
- [Cleaning](#cleaning)
- [Analysis](#analysis_model-training_and_evaluation)
- [Conclusion](#conclusion)
- [Future Work](#future-work)
- [Links](#links)

## Project Description
This project aims to create a timeseries forecast to predict sales based on historical sales data for 1,115 Rossmann stores. Note that some stores in the dataset were temporarily closed for refurbishment.


## Hypotheses / Questions
Rossman closed nearly 200 stores for a period of six months for renovation. Does that affect the model negatively?
* if yes, How can we create a model that would predict the sales after they opened?

## Dataset
The data & Data Description is available here: https://www.kaggle.com/c/rossmann-store-sales/data


## Cleaning
Data was relatively clean since in a timeseries, we only need a few columns.
I created some functions that aggregated month data or helped in the preprocessing.

## Analysis, Model Training, and Evaluation
* Plotting data
* Inspected holidays
* Created fb Prophet models, check residuals, iterate, check again.. etc
* Created for-loops to hypertune models, and used Auto-Arima** from the pmdarima Library for checking residual RSME


## Conclusion
* Summarize your results. What do they mean?
* What can you say about your hypotheses?
* Interpret your findings in terms of the questions you try to answer.

## Future Work
- Create a model for each store / or bins of stores.
- Use competitor data for a complementary model.


## Links
[Repository](https://github.com/Faisal7ammad/Project-Week-8-Final-Project)  
[Slides](https://docs.google.com/presentation/d/1wk9iASfi8rPyScNvLtEniumgv6QKyLzAJ3LGOIeespM/edit?usp=sharing)    
