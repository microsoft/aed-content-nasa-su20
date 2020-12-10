# Local Machine Learning: Logistic Regression

One of the models not tested by Azure Machine Learning was logistic regression. The logistic regression algorithm fits a logistic (s-shaped) curve over data points in order to classify them into two categories (such as 'launched' and 'delayed'). It is a popular classifier because it can also convey the relative importance of different features in a model. However, in order to build a model that can accurately give us this information, we will need to clean our data more.

## Further Data Cleansing and Preparation

First, we will check the features for multicollinearity. While collinear features will not impact model performance, it will interfer with the coefficients of the fitted model, and those coefficients can be some of the most interesting information for understanding the model and the data.

The variance inflation factor (VIF) is a common statistical tool used to check for collinearity of features in the data. It essentially looks for $\dfrac{1}{1-R^2}$, so a lower number is better (in that it denotes features that not collinear with other features).

Import `variance_inflation_factor` from `statsmodels.stats.outliers_influence` and create a function to measure the VIF for each column. Return the results in a pandas Series to make it easy to see which columns are collinear.

```python
from statsmodels.stats.outliers_influence import variance_inflation_factor

def calculate_vif(X):
    vif_list = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    return(pd.Series(vif_list, index=X.columns))
```

```python
calculate_vif(df.iloc[:, :-1])
```

```output
Day of Year      1.35
Time             1.10
Temp             2.76
Percipitation    2.09
Wind Speed       1.38
Visibility       1.10
Day Length       2.32
Cloudy          50.77
Fair            39.02
Heavy T-Storm    4.31
Partly Cloudy   39.93
Rain             7.54
dtype: float64
```
Several of our dummy variables are collinear. This a result of having too many dummy variables. One of the dummy variables is a linear combination of the other dummary variables, which is the definition of multicollinearity.

Generate the dummy variables anew. It will be easiest to do this by first reverting back to the backup copy of `df`.

```python
df = df_backup.copy(deep=False)
df.head()
```

| <br>Name | Day of Year | Time | Launched | Temp | Percipitation | Wind Speed | Visibility | Day Length | Condition |
|---|---|---|---|---|---|---|---|---|---|									
| Pioneer 3 | 340 | 105 | 1 | 62.00 | 0.00 | 11.00 | 10 | 625 | Cloudy |
| Pioneer 4 | 62 | 790 | 1 | 78.00 | 0.00 | 12.00 | 7 | 698 | Cloudy |
| Ranger 1 | 235 | 664 | 1 | 90.00 | 0.00 | 9.00 | 10 | 776 | Partly Cloudy |
| Ranger 2 | 322 | 549 | 1 | 54.00 | 0.00 | 6.00 | 15 | 641 | Fair |
| Ranger 3 | 26 | 1290 | 1 | 53.00 | 0.00 | 17.00 | 10 | 645 | Fair |

Re-create the dummy variables, this time dropping the first one (Cloudy); cloudy days can be deduced as those rows that are a 0 for each of the other dummy columns.

```python
dummy = pd.get_dummies(df['Condition'], drop_first=True)
df = pd.concat([df.iloc[:, :-1], dummy], axis=1)

column_list = list(df)
launched = column_list.pop(2)
column_list.append(launched)

df = df[column_list]
df.head()
```

| <br>Name | Day of Year | Time | Temp | Percipitation | Wind Speed | Visibility | Day Length | Fair | Heavy T-Storm | Partly Cloudy | Rain | Launched |
|---|---|---|---|---|---|---|---|---|---|---|---|---|												
| Pioneer 3 | 340 | 105 | 62.00 | 0.00 | 11.00 | 10 | 625 | 0 | 0 | 0 | 0 | 1 |
| Pioneer 4 | 62 | 790 | 78.00 | 0.00 | 12.00 | 7 | 698 | 0 | 0 | 0 | 0 | 1 |
| Ranger 1 | 235 | 664 | 90.00 | 0.00 | 9.00 | 10 | 776 | 0 | 0 | 1 | 0 | 1 |
| Ranger 2 | 322 | 549 | 54.00 | 0.00 | 6.00 | 15 | 641| 1 | 0 | 0 | 0 | 1 |
| Ranger 3 | 26 | 1290 | 53.00 | 0.00 | 17.00 | 10 | 645 | 1  | 0 | 0 | 0 | 1 |

Now check for multicollinearity again.

```python
calculate_vif(df.iloc[:, :-1])
```

```output
Day of Year       5.08
Time              8.83
Temp            157.59
Percipitation     2.18
Wind Speed        8.25
Visibility        3.18
Day Length      160.49
Fair              2.20
Heavy T-Storm     1.32
Partly Cloudy     1.87
Rain              2.10
dtype: float64
```

The dummy variables are no longer collinear, but two other features now register as such: `Temp` and `Day Length`. And that makes sense: both of those values would be highly correlated with the time of year. Let's remove those two columns using the `drop()` method (with `inplace=True`).

```python
df.drop(columns=['Temp', 'Day Length'], inplace=True)
df.head()
```

| <br>Name | Day of Year | Time | Percipitation | Wind Speed | Visibility | Fair | Heavy T-Storm | Partly Cloudy | Rain | Launched |
|---|---|---|---|---|---|---|---|---|---|---|										
| Pioneer 3 | 340 | 105 | 0.00 | 11.00 | 10 | 0 | 0 | 0 | 0 | 1 |
| Pioneer 4 | 62 | 790 | 0.00 | 12.00 | 7 | 0 | 0 | 0 | 0 | 1 |
| Ranger 1 | 235 | 664 | 0.00 | 9.00 | 10 | 0 | 0 | 1 | 0 | 1 |
| Ranger 2 | 322 | 549 | 0.00 | 6.00 | 15 | 1 | 0 | 0 | 0 | 1 |
|Ranger 3 | 26 | 1290 | 0.00 | 17.00 | 10 | 1 | 0 | 0 | 0 | 1 |

And a final check for collinearity. Everything should check out and be ready for fitting the logistic regression model.

```python
calculate_vif(df.iloc[:, :-1])
```

```output
Day of Year     3.48
Time            5.06
Percipitation   2.16
Wind Speed      5.70
Visibility      2.96
Fair            1.71
Heavy T-Storm   1.30
Partly Cloudy   1.63
Rain            1.99
dtype: float64
```

## Train Model

Because we have changed our columns, we need to redefine `X` and `y`.

```python
X = df.iloc[:, :-1].to_numpy()
y = df.iloc[:, -1]
```

Import `LogisticRegression` from `sklearn.linear_model` and fit the model.

```python
from sklearn.linear_model import LogisticRegression

logr = LogisticRegression()
logr.fit(X, y)
```

```output
LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,
                   intercept_scaling=1, l1_ratio=None, max_iter=100,
                   multi_class='auto', n_jobs=None, penalty='l2',
                   random_state=None, solver='lbfgs', tol=0.0001, verbose=0,
                   warm_start=False)
```

Now import test data with the correct number of columns.

```python
test_df = pd.read_csv('test_data.csv')
test_df.set_index('Name', inplace=True)
test_df
```

| <br>Name | Day of Year | Time | Percipitation | Wind Speed | Visibility | Fair | Heavy T-Storm | Partly Cloudy | Rain | Launched |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | Kerbal 1 | 338 | 1203 | 0.00 | 72 | 10 | 0 | 0 | 0 | 0 | 0 |
| 1 | Kerbal 2 | 75 | 1061 | 0.00 | 4 | 1 | 0 | 0 | 0 | 0 | 1 |
| 2 | Kerbal 3 | 154 | 879 | 0.28 | 6 | 15 | 0 | 0 | 0 | 1 | 1 |
| 3 | Kerbal 4 | 155 | 781 | 16.00 | 6 | 15 | 0 | 1 | 0 | 0 | 0 |
| 4 | Kerbal 5 | 140 | 993 | 0.00 | 25 | 10 | 1 | 0 | 0 | 0 | 1 |

## Predict Delays

Now test the model.

```python
test_df.set_index('Name', inplace=True)

test_X = test_df.iloc[:, :-1].to_numpy()
pred_y = logr.predict(test_X)
pred_y
```

```output
array([0, 1, 1, 1, 1], dtype=int64)
```

Let's check predicted probabilities of delay.

```python
lprobs = logr.predict_proba(test_X)
lprobs
```

```output
array([[1.00000000e+00, 2.87449119e-11],
       [7.58992270e-06, 9.99992410e-01],
       [2.04184518e-05, 9.99979582e-01],
       [7.04224888e-04, 9.99295775e-01],
       [4.59069145e-01, 5.40930855e-01]])
```

With the scientific notation, this is even harder to read. Let's print out the more readable format.

```python
for i in range(len(test_df.index)):
    print(test_df.index[i] + ' probability of delay is {:.2%}'.format(lprobs[i][0]))
```

```output
Kerbal 1 probability of delay is 100.00%
Kerbal 2 probability of delay is 0.00%
Kerbal 3 probability of delay is 0.00%
Kerbal 4 probability of delay is 0.07%
Kerbal 5 probability of delay is 45.91%
```

Unlike extra random trees, we can't directly see how features are weighted, but we can see the actual coefficients of the regression model. (This is why we took so much time to eliminate collinearity among the features: so we can get accurate coefficients.) Use the first `coef_` attribute for the model to see this (and put it in a Series for readability).

```python
pd.Series(logr.coef_[0], index=df.iloc[:, :-1].columns)
```

```output
Day of Year     -0.00
Time             0.00
Percipitation   -0.15
Wind Speed      -0.54
Visibility       0.06
Fair            -0.52
Heavy T-Storm   -0.71
Partly Cloudy    0.06
Rain             0.08
dtype: float64
```

This model is the opposite of our extra random trees model: highly sensitive to wind speed, less so to thunderstorms. (The coefficient for Heavy T-Storm is higher, but keep in mind that that is the coefficient for a binary variables while the smaller coefficient for Wind Speed will be multiplied by the actual value of the wind speed.)

Finally, let's examine the precision and accuracy of the logistic regression model.

```python
print('Logistic-regression precision: {}'.format(sklearn.metrics.precision_score(true_y, pred_y)))
print('Logistic-regression accuracy: {}'.format(sklearn.metrics.accuracy_score(true_y, pred_y)))
```

```output
Logistic-regression precision: 0.75
Logistic-regression accuracy: 0.8
```

Because both the logistic regression and the extra random trees models each had one true negative and one false positive, they both have the same precision and accuracy scores.