# Exercise - Predict the Success of a Rocket Launch using Machine Learning

Our AI system will help to decide if we should launch a rocket or not. 
![launch](launch_images/mlmodel.png)

```Python
# ['Crewed or Uncrewed', 'High Temp', 'Low Temp', 'Ave Temp',
#        'Temp at Launch Time', 'Hist High Temp', 'Hist Low Temp',
#        'Hist Ave Temp', 'Percipitation at Launch Time',
#        'Hist Ave Percipitation', 'Wind Direction', 'Max Wind Speed',
#        'Visibility', 'Wind Speed at Launch Time', 'Hist Ave Max Wind Speed',
#        'Hist Ave Visibility', 'Condition']

tree_model.predict([[ 1.  , 75.  , 68.  , 71.  ,  0.  , 75.  , 55.  , 65.  ,  0.  , 0.08,  0.  , 16.  , 15.  ,  0.  ,  0.  ,  0.  ,  0.  ]])
```