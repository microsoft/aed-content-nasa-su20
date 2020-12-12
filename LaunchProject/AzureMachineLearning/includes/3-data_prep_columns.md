# Data Preparation Part 1 - Preliminary Steps

A primary reason to use an cloud-based service like Azure Machine Learning is that it simplifies not just the machine-learning part of data science (such as model selection and feature engineering), but also data cleansing. However, we should still take an initial look at our data and do some light cleaning and preparation before uploading it to Azure. We'll start here with dropping unnecessary columns in the dataset.

## Import Libraries and Data

Start by importing two of the standard libraries for data science in Python: pandas and numpy.

```python
import pandas as pd
import numpy as np
```

No import the rocket-launch data, which is in a CSV file.

```python
data_df = pd.read_csv('RocketLaunchDataCompleted.csv')
data_df.head()
```

**output**

| | Name | Date | Time (East Coast) | Location | Crewed or Uncrewed | Launched? | High Temp | Low Temp | Ave Temp | Temp at Launch Time | ... | Max Wind Speed | Visibility | Wind Speed at Launch Time | Hist Ave Max Wind Speed | Hist Ave Visibility | Sea Level Pressure | Hist Ave Sea Level Pressure | Day Length | Condition | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | NaN | 4-Dec-58 | NaN | Cape Canaveral | NaN | NaN | 75 | 68 | 71.00 | NaN | ... | 16 | 15 | NaN | NaN | NaN | 30.22 | NaN | 10:26 | Cloudy | NaN |
| 1 | NaN | 5-Dec-58 | NaN | Cape Canaveral | NaN | NaN | 78 | 70 | 73.39 | NaN | ... | 14 | 10 | NaN | NaN | NaN | 30.2 | NaN | 10:26 | Cloudy | NaN |
| 2 | Pioneer 3 | 6-Dec-58 | 1:45 | Cape Canaveral | Uncrewed | Y | 73 | 0 | 60.21 | 62.0 | ... | 15 | 10 | 11.0 | NaN | NaN | 30.25 | NaN | 10:25 | Cloudy | NaN |
| 3 | NaN | 7-Dec-58 | NaN | Cape Canaveral | NaN | NaN | 76 | 57 | 66.04 | NaN | ... | 10 | 10 | NaN | NaN | NaN | 30.28 | NaN | 10:25 | Partly Cloudy | NaN |
| 4 | NaN | 8-Dec-58 | NaN | Cape Canaveral | NaN | NaN | 79 | 60 | 70.52 | NaN | ... | 12 | 10 | NaN | NaN | NaN | 30.23 | NaN | 12:24 | Partly Cloudy | NaN |

## Check for missing data and conduct basic data cleansing

Just looking at the first five lines, there are a lot of `NaN` values in the DataFrame. `NaN` is a reserved floating-point value that stands for 'not a number.' It is what pandas uses where there is no value (such as when a cell in an imported Excel spreadsheet is empty).

To get some idea of just how many `NaN` values our DataFrame has, look first at the shape of the DataFrame to find the total number of columns and rows.

```python
data_df.shape
```

```output
(299, 26)
```

Now use the `isna()` and `sum()` methods for the DataFrame. The first pandas method flags values in DataFrame columns as `NaN` or not; the second builds on this and adds up all of the instances of `NaN` in each column. (One of the great features of pandas is that we can tack methods one after another on pandas objects to create concise, powerful code.)

```python
data_df.isna().sum()
```

```output
Name                            240
Date                              0
Time (East Coast)               241
Location                          0
Crewed or Uncrewed              240
Launched?                       240
High Temp                         0
Low Temp                          0
Ave Temp                          0
Temp at Launch Time             240
Hist High Temp                    0
Hist Low Temp                     0
Hist Ave Temp                     0
Percipitation at Launch Time      0
Hist Ave Percipitation            0
Wind Direction                    0
Max Wind Speed                    0
Visibility                        0
Wind Speed at Launch Time       240
Hist Ave Max Wind Speed         299
Hist Ave Visibility             299
Sea Level Pressure                0
Hist Ave Sea Level Pressure     299
Day Length                        1
Condition                         1
Notes                           296
dtype: int64
```

We have three columns that contain nothing but `NaN` values. A simple way to delete them is to use the pandas `dropna()` method. The `axis='columns'` parameter in the method will have it work on the columns of the DataFrame as opposed to the rows; the `how='all'` parameter will have it remove columns that are all `NaN`s; and the `inplace='True'` parameter will perform the column-removal in the existing DataFrame (rather than creating a new object).

```python
data_df.dropna(axis='columns', inplace=True, how='all')
data_df.isna().sum()
```

```output
Name                            240
Date                              0
Time (East Coast)               241
Location                          0
Crewed or Uncrewed              240
Launched?                       240
High Temp                         0
Low Temp                          0
Ave Temp                          0
Temp at Launch Time             240
Hist High Temp                    0
Hist Low Temp                     0
Hist Ave Temp                     0
Percipitation at Launch Time      0
Hist Ave Percipitation            0
Wind Direction                    0
Max Wind Speed                    0
Visibility                        0
Wind Speed at Launch Time       240
Sea Level Pressure                0
Day Length                        1
Condition                         1
Notes                           296
dtype: int64
```

The `Notes` column is also almost entirely `NaN`s as well and won't be useful for machine learning anyway, so remove that column manually using the `drop()` method (setting `columns=['Notes']` and `inplace=True`)

```python
data_df.drop(columns=['Notes'], inplace=True)
data_df.isna().sum()
```

```output
Name                            240
Date                              0
Time (East Coast)               241
Location                          0
Crewed or Uncrewed              240
Launched?                       240
High Temp                         0
Low Temp                          0
Ave Temp                          0
Temp at Launch Time             240
Hist High Temp                    0
Hist Low Temp                     0
Hist Ave Temp                     0
Percipitation at Launch Time      0
Hist Ave Percipitation            0
Wind Direction                    0
Max Wind Speed                    0
Visibility                        0
Wind Speed at Launch Time       240
Sea Level Pressure                0
Day Length                        1
Condition                         1
dtype: int64
```