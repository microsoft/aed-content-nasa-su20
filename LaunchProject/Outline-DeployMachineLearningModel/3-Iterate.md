# Exercise - Improve a Machine Learning Model through Iteration

Add some data, run it again

```Python

```

```Python
# Create decision tree classifer 
tree_model_2 = DecisionTreeClassifier(random_state=0,max_depth=5)

X_train_2, X_test_2, y_train_2, y_test_2 = train_test_split(X,y, test_size=0.2, random_state=99)

# Fitting the model to the training data
tree_model_2.fit(X_train_2,y_train_2)

# Do prediction on test Data
y_pred_2=tree_model_2.predict(X_test_2)
print(y_pred_2)
```