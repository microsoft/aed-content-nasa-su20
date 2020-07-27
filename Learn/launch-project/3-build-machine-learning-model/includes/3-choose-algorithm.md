# Exercise - Choose the Machine Learning Algorithm to Predict Rocket Launch Success

After we have told that computer which columns we want to look at to make predictions, we will need to tell the computer which algorithm to use to make our model. You can look at a variety of different algorithms that will make different machine learning models, but for our example we will be using a decision tree. A decision tree is a very good introduction algorithm because it is eay to think about. The way it works is by either choosing one branch of the other.

Algorithm Cheat Sheet

```Python
# Create decision tree classifer 
tree_model = DecisionTreeClassifier(random_state=0,max_depth=5)
```

Next, we will build a machine learning algorithm to digest our data and find best weather patters for a launch 
- Machine learning algorithms take the data and return the insights about what are indicators of good rocket launch days
- We show these associations with links such as shown below:<br>