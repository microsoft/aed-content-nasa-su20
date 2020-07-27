# Exercise - Determine Features to Include in a Machine Learning Model

To begin training our machine learning model, we will start by teaching the computer what parts of the data to look at to make predictions. We know that the column that we are interested in the model to predict is the "Launched" column, so we will extract this column and store it in a variable.

Next, we will remove some of the columns that are not needed for making this prediction. Columns like "Name" are great for humans to give us more context about the data, but they are pretty unnecessary for computers. In this example, we are very interested in the columns involving wind speed, conditions, and precipitation.

```Python
# First we select the output we are interested in, in this case "launch" yes and no's. 
y=lanch_data['Launched?']
# removing the columns we are not interested in
lanch_data.drop(['Name','Date','Time (East Coast)','Location','Launched?','Hist Ave Sea Level Pressure','Sea Level Pressure','Day Length','Notes'],axis=1, inplace=True)
X=lanch_data
```

Maybe add some actual featurization here

```Python
# list of variables that our machine learning algorithm is going to look at:
X.columns
```