# Exercise - Split Data into Training and Testing Datasets

After we have choose the algorithm that we want, we must split our data into a training and testing group. We have a lump of data right now, but in order to train the model, we must choose some of this data to actually train the model and some of it to test it to ensure it is making accurate predictions. 

The code below will randomly separate the data we have into four groups. It is very important that the data is randomly choose because if not, it could be very wrong when making predictions. Also, as you can see the code specifies that the test size is 0.2. This means that the testing groups will have 20% of the data while the training groups will have 80%. It is generally a good idea to make the testing group larger because this will yield the best predictions.

```Python
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=99)
```