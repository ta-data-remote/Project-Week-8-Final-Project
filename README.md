<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Predicting Titanic survivors with Machine Learning
*[Aleksandar Nikolov]*

*[DATA FT MAY, REMOTE, 2021]*

## Content
- [Project Description](#project-description)
- [Hypotheses / Questions](#hypotheses-questions)
- [Dataset](#dataset)
- [Cleaning](#cleaning)
- [Analysis](#analysis)
- [Model Training and Evaluation](#model-training-and-evaluation)
- [Conclusion](#conclusion)
- [Future Work](#future-work)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Project Description
This project is about binary classification problem. The basic idea is to predict whether passenger survived or died in Titanic shipwreck.

## Hypotheses / Questions
* How many people died or survived?
* How do age affect survival rate?
* How do gender affect survival rate
* How do passenger's class affect survival rate?
* How do siblings and spouses affect survival rate?
* How do port of embarkation affect survival rate?
 
## Dataset
* The dataset was provided by Kaggle.
* Data contain information about passenger's name, age, gender, class, cabin, whether he or she has siblings or spouses on board and ho wmany, the same for parents and children and where embarked on board.
* In train dataset there is information whether passenger survived or not.  



## Cleaning
* AGE -  filling with KNN-Imputation method, which takes information from all other variables and predict the most possible value for age.
* CABIN - dropped, because it has 687 out of 891 missing values and it's quite hard to be filled.
* EMBARKED - filling with mode, which is S.
* Outliers were detected based on boxplot analysis and dropped based on standard deviation approach.
* PassengerID, Name, Ticket were dropped while building the model.  

## Analysis
* 10 different models were used to solve this binary classification problem. (Logistic Regression, Random Forest Classifier, Catboost Classifier and so on.)
* The best performing models were KNN and Catboost.
* Combining both models lead to slightly worst results.

## Model Training and Evaluation
* The final model was Catboost with accuracy score of 0.81 and kappa score 0.82

## Conclusion
* The resulst are satisfactorily but there is still place for improvements.

## Future Work
* Different strategies for fillin missing values and handling outliers.
* NLP for extracting valuable information from names, like title.

## Workflow
* The work was divided in 4 main steps.
* 1. Create a plan
* 2. Clean the data 
* 3. Data visualization 
* 4. Building a model 

## Organization
* A trello board was used to organize the work.
* The repo has two directories, one for the code and one for the data. 
* The code directory includes three files, one for the data cleaning, visualizations, and predictions.
* The data directory contains initial data sets (train and test) and cleaned data set for visualizations and modeling.



## Links

[Dataset](https://www.kaggle.com/c/titanic/data)
[Presentation](https://drive.google.com/file/d/1RwQuYr2FTdweED14OyLF0xVsUco3t5os/view?usp=sharing)  
[Trello](https://trello.com/b/JcT6ox3A/titanic-final-project-ironhack)  
