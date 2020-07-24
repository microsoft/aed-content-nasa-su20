# Exercise - Determine Features to Include in a Machine Learning Model

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