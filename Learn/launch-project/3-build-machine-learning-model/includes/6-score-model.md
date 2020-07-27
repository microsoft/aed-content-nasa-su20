# Exercise - Score the Machine Learning Model that Predicts Rocket Launch Success

To access how well our model is at predicting, we wil use the `.score` function to see how well the predictions matches the actual results. If the score is higher, this means that our model is better at predicting the outcome.

```Python
# Calculate accuracy
tree_model.score(X_test,y_test)
```
