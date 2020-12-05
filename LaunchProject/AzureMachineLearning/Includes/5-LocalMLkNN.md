# Local Machine Learning: k-Nearest Neighbors

The $k$-Nearest Neighbors algorithm (k-NN for short) classifies objects based on the classification of the nearest $k$ training examples. 'Nearest' in this case refers to numeric distance, which is why we went through so much effort to convert all of our dataset features into numeric values.

k-NN is a fairly intuitive algorithm, so it makes a good starting point for exploring machine learning with our dataset.

## Train Model

Our first task will be to define our training data. We want every column except `Launched` to serve as our features and `Launched` itself to be our label (the value we are trying to predict or classify). By convention, we use `X` for the features and `y` for the label. (Because we need to separate out the columns, it is often convenient to make the label the final column of a DataFrame.)

Note that many scikit-learn algorithms require the input to be in numpy arrays.

```python
X = df.iloc[:, :-1].to_numpy()
y = df.iloc[:, -1]
```

Now we need to import the `KNeighborsClassifier` algorithm from `sklearn.neighbors`, create the model object, and fit the model.

```python
from sklearn.neighbors import KNeighborsClassifier

neigh = KNeighborsClassifier()
neigh.fit(X, y)
```

```output
KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
                     metric_params=None, n_jobs=None, n_neighbors=5, p=2,
                     weights='uniform')
```

As in the Azure Machine Learning module, our original dataset has only one delayed rocket launch in it, so a traditional test-training split is not appropriate. Instead, we will import a synthesized test dataset with two delayed launches, one for extremely high winds and one for thunderstorms.

```python
test_df = pd.read_csv('test_data_full.csv')
test_df
```

```output
| Name | Day of Year | Time | Temp | Percipitation | Wind Speed | Visibility | Day Length | Cloudy | Fair | Heavy T-Storm | Partly Cloudy | Rain | Launched |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | Kerbal 1 | 338 | 1203 | 63 | 0.00 | 72 | 10 | 644 | 1 | 0 | 0| 0 | 0 | 0 |
| 1 | Kerbal 2 | 75 | 1061 | 79 | 0.00 | 4 | 1 | 702 | 1 | 0 | 0 | 0 | 0 | 1 |
| 2 | Kerbal 3 | 154 | 879 | 83 | 0.28 | 6 | 15 | 801 | 0 | 0 | 0 | 0 | 1 | 1 |
| 3 | Kerbal 4 | 155 | 781 | 69 | 16.00 | 6 | 15 | 802 | 0 | 0 | 1 | 0 | 0 |
| 4 | Kerbal 5 | 140 | 993 | 78 | 0.00 | 25 | 10 | 778 | 0 | 1 | 0 | 0 | 0 | 1 |
```

Before proceding, make sure to make `Name` the index for this DataFrame so as to match up with the training data.

```python
test_df.set_index('Name', inplace=True)
test_df.head()
```

```output
| <br>Name | Day of Year | Time | Temp | Percipitation | Wind Speed | Visibility | Day Length | Cloudy | Fair | Heavy T-Storm | Partly Cloudy | Rain | Launched |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|													
| Kerbal 1 | 338 | 1203 | 63 | 0.00 | 72 | 10 | 644 | 1 | 0 | 0 | 0 | 0 | 0 |
| Kerbal 2 | 75 | 1061 | 79 | 0.00 | 4 | 1 | 702 | 1 | 0 | 0 | 0 | 0 | 1 |
| Kerbal 3 | 154 | 879 | 83 | 0.28 | 6 | 15 | 801 | 0 | 0 | 0 | 0 | 1 | 1 |
| Kerbal 4 | 155 | 781 | 69	16.00 | 6 | 15 | 802 | 0 | 0 | 1 | 0 | 0 | 0 |
| Kerbal 5 | 140 | 993 | 78 | 0.00 | 25 | 10 | 778 | 0 | 1 | 0 | 0 | 0 | 1 |
```

## Predict Delays

Now that we have the test data, let's predict probable delays. Create an array called `X_test` and use it with the `predict()` method in out model object to predict `y` values. (Note that `1` refers to a probable launch and `0` to a probable delay.)

```python
test_X = test_df.iloc[:, :-1].to_numpy()
pred_y = neigh.predict(test_X)
pred_y
```

```output
array([1, 1, 1, 1, 1], dtype=int64)
```

k-NN predicts no delays, so we should take a closer look at the actual output of the model. To do so, use the `predict_proba()` to see the actual probabilities of launch and delay.

```python
probs = neigh.predict_proba(test_X)
probs
```

```output
array([[0. , 1. ],
       [0.2, 0.8],
       [0. , 1. ],
       [0. , 1. ],
       [0.2, 0.8]])
```

This gives shows that two of these launches have at least some probability of delay, but it is kind of hard to ready. Let's print this out again in a easier-to-read format.

```python
for i in range(len(test_df.index)):
    print(test_df.index[i] + ' probability of delay is {:.0%}'.format(probs[i][0]))
```

```output
Kerbal 1 probability of delay is 0%
Kerbal 2 probability of delay is 20%
Kerbal 3 probability of delay is 0%
Kerbal 4 probability of delay is 0%
Kerbal 5 probability of delay is 20%
```

Much easier to read. k-NN caught the two test missions that were delayed, but the probabilities seem low (and suspiciously regular).

With a little more coding, we can loop through different number of neighbors to looke for patterns (the default is `k=5`). To this, we will create a dictionary for each mission and then check the predicted probability for delay for each mission for 3 to 20 neighbors. We can then put those five dictionaries into a DataFrame to make final output easier to read.

```python
kerbal_dict = {'Kerbal ' + str(x):[] for x in range(1, 6)}
idx_list = list(range(3, 21))

for i in idx_list:
    ineigh = KNeighborsClassifier(n_neighbors=i)
    ineigh.fit(X, y)
    for j in range(len(kerbal_dict)):
        kerbal_dict['Kerbal ' + str(j + 1)].append(ineigh.predict_proba(test_X)[j][0])

kerbal_df = pd.DataFrame(kerbal_dict, index=idx_list)
kerbal_df
```

```output
Kerbal 1	Kerbal 2	Kerbal 3	Kerbal 4	Kerbal 5
3	0.00	0.00	0.00	0.00	0.33
4	0.00	0.00	0.00	0.00	0.25
5	0.00	0.20	0.00	0.00	0.20
6	0.00	0.17	0.00	0.00	0.17
7	0.00	0.14	0.00	0.00	0.14
8	0.00	0.12	0.00	0.00	0.12
9	0.00	0.11	0.00	0.00	0.11
10	0.00	0.10	0.10	0.00	0.10
11	0.00	0.09	0.09	0.00	0.09
12	0.00	0.08	0.08	0.00	0.08
13	0.00	0.08	0.08	0.00	0.08
14	0.00	0.07	0.07	0.00	0.07
15	0.00	0.07	0.07	0.00	0.07
16	0.00	0.06	0.06	0.00	0.06
17	0.00	0.06	0.06	0.00	0.06
18	0.00	0.06	0.06	0.06	0.06
19	0.00	0.05	0.05	0.05	0.05
20	0.00	0.05	0.05	0.05	0.05
```

So the problem stems from our training data. There is only one delayed launch and the probability of classifying a new test case as 'delayed' and the way that the k-NN algorithm works, the highest probability that k-NN can give to a negative classification like 'delayed' is the number of training example (in this case, 1) divided by the number of neighbors. (k-NN is extremely sensitive to the underlying data structure.)

As a final bit of investigation into our k-NN model, let's look at its precision and accuracy. The `sklearn.metrics` has `precision_score()` and `accuracy_score()` functions for this.

```python
import sklearn.metrics

true_y = test_df['Launched']
print('Nearest-neighbors precision: {}'.format(sklearn.metrics.precision_score(true_y, pred_y)))
print('Nearest-neighbors accuracy: {}'.format(sklearn.metrics.accuracy_score(true_y, pred_y)))
```

```output
Nearest-neighbors precision: 0.6
Nearest-neighbors accuracy: 0.6
```

Both the precision and accuracy of our k-NN model is rather low. Let's move on to see if other algorithms provide better insights and results.