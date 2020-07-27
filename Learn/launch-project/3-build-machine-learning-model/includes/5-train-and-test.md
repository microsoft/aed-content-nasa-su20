# Exercise - Train and Test the Machine Learning Model to Predict Rocket Launch Success

After the data is separated into the training and testing sections, we can train our machine learning model. Thanks to all of the libraries that we have imported, this is as simple as writing a few lines of code. Using the variable that stored the decision tree we created a few units ago, we can just call the `.fit` function with our training data to being the training process. Fitting the data basically means training it.

```Python
# Fitting the model to the training data
tree_model.fit(X_train,y_train)

# Do prediction on test Data
y_pred=tree_model.predict(X_test)
print(y_pred)
```

After the data is fit to the model, we can call the `.predict` function to use the model to predict if a launch will be delayed or not in the testing group.
