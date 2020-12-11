# Data Preparation

A primary reason to use an cloud-based service like Azure Machine Learning is that it simplifies not just the machine-learning part of data science (such as model selection and feature engineering), but also data cleansing. However, we should still take an initial look at our data and do some light cleaning and preparation before uploading it to Azure.

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

## Check for and remove rows with NaNs for recorded launches

The DataFrame is trimmed down, but we still have a lot of columns in which the majority of the entries are `NaN`. However, one of those columns is `Launched?`, which tells us if a rocket launch at the Kennedy Space Center actually went ahead, so we cannot just drop these columns. Instead, you will have to drop just to those rows that have `NaN` values in the `Launched?` column.

Drop these rows by using a mask. A mask is just a Boolean flag to applied to entries in a pandas Series or DataFrame based on some condition. For example, this code snippet creates a mask that reads `True` for values in the `Launched?` column that are not `NaN`:

```python
mask = data_df['Launched?'].notna()
mask
```

```output
0      False
1      False
2       True
3      False
4      False
       ...  
294    False
295    False
296     True
297    False
298    False
Name: Launched?, Length: 299, dtype: bool
```

We can apply it to the DataFrame using its `.loc` attribute. By default, `.iloc` returns DataFrame rows based on labels, such as row names or a mask. It has no `inplace` attribute, so we apply the mask to the DataFrame using `.loc` this way:

```python
launch_df = data_df.loc[mask]
launch_df.tail()
```

**output**

| | Name | Date | Time (East Coast) | Location | Crewed or Uncrewed | Launched? | High Temp | Low Temp | Ave Temp | Temp at Launch Time | ... | Hist Ave Temp | Percipitation at Launch Time | Hist Ave Percipitation | Wind Direction | Max Wind Speed | Visibility | Wind Speed at Launch Time | Sea Level Pressure | Day Length | Condition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 276 | Gemini 7 | 4-Dec-65 | 20:03 | Cape Canaveral | Crewed | Y | 77 | 67 | 71.52 | 71.0 | ... | 65.0 | 0.00 | 0.08 | E | 15 | 10 | 12.0 | 30.19 | 10:27 | Cloudy |
| 281 | Gemini 8 | 16-Mar-66 | 17:41 | Cape Canaveral | Crewed | Y | 85 | 0 | 64.81 | 80.0 | ... | 66.0 | 0.00 | 0.11 | S | 16 | 15 | 4.0 | 29.95 | 12:00 | Cloudy |
| 286 | Gemini 9A | 3-Jun-66 | 14:39 | Cape Canaveral | Crewed | Y | 87 | 0 | 74.40 | 83.0 | ... | 79.0 | 0.00 | 0.19 | E | 15 | 15 | 6.0 | 29.96 | 13:49 | Cloudy |
| 291 | Space X Dragon | 27-May-20 | 16:33 | Cape Canaveral | Crewed | N | 86 | 70 | 75.02 | 74.0 | ... | 79.0 | 0.28 | 0.15 | S | 32 | 10 | 25.0 | 29.98 | 13:44 | Heavy T-Storm |
| 296 | Space X Dragon | 30-May-20 | 20:22 | Cape Canaveral | Crewed | Y | 87 | 75 | 79.69 | 80.0 | ... | 79.0 | 0.00 | 0.16 | SE | 16 | 10 | 7.0 | 30.03 | 13:47 | Fair |
5 rows × 22 columns

We now have a DataFrame with just valid entries in the `Launched?` column. You can double-check this by using the DataFrame's `isna()` and `sum()` methods again.

```python
launch_df.isna().sum()
```

```output
Name                            0
Date                            0
Time (East Coast)               1
Location                        0
Crewed or Uncrewed              0
Launched?                       0
High Temp                       0
Low Temp                        0
Ave Temp                        0
Temp at Launch Time             0
Hist High Temp                  0
Hist Low Temp                   0
Hist Ave Temp                   0
Percipitation at Launch Time    0
Hist Ave Percipitation          0
Wind Direction                  0
Max Wind Speed                  0
Visibility                      0
Wind Speed at Launch Time       0
Sea Level Pressure              0
Day Length                      0
Condition                       0
dtype: int64
```

We still have a lingering `NaN` value in the `Time (East Coast)` column, but you can leave that be for now.

## Create DataFrame for module and rename columns for concision

The DataFrame is much more streamlined now. However, we likely don't need all of these features for our machine learning. For example, use the `value_counts()` method on the `Location` column to see how many of what values are in that column.

```python
launch_df['Location'].value_counts()
```

```output
Cape Canaveral    51
Kennedy            8
Name: Location, dtype: int64
```

Given that Cape Canaveral is simply the old name for the Kennedy Space Center, this column tells us nothing and thus can't provide any value in a machine-learning model. We should remove it, or at least not retain it.

There are other features in our dataset that are of questionable value to our models, such as historic average precipitation. Given the number of these, it will be easier to select those features most useful to us (name, data, time, temperature, precipitation, wind speed, day length, condition) and create a new DataFrame.

```python
df = launch_df[['Name', 
                'Date', 
                'Time (East Coast)', 
                'Launched?', 
                'Temp at Launch Time', 
                'Percipitation at Launch Time', 
                'Wind Speed at Launch Time', 
                'Visibility', 
                'Day Length', 
                'Condition']]
df.head()
```

**output**

| | Name | Date | Time (East Coast) | Launched? | Temp at Launch Time | Percipitation at Launch Time | Wind Speed at Launch Time | Visibility | Day Length | Condition |
|---|---|---|---|---|---|---|---|---|---|---|
| 2 | Pioneer 3 | 6-Dec-58 | 1:45 | Y | 62.00 | 0.00 | 11.00 | 10 | 10:25 | Cloudy |
| 7 | Pioneer 4 | 3-Mar-59 | 13:10 | Y | 78.00 | 0.00 | 12.00 | 7 | 11:38 | Cloudy |
| 12 | Ranger 1 | 23-Aug-61 | 11:04 | Y | 90.00 | 0.00 | 9.00 | 10 | 12:56 | Partly Cloudy |
| 17 | Ranger 2 | 18-Nov-61 | 9:09 | Y | 54.00 | 0.00 | 6.00 | 15 | 10:41 | Fair |
| 22 | Ranger 3 | 26-Jan-62 | 21:30 | Y | 53.00 | 0.00 | 17.00 | 10 | 10:45 | Fair |

We retained the names of the missions that launched as a convenient way to identify them. Given that they are unique, we can use them as the index for this new DataFrame in place of the default integer index assigned by pandas (which is in tatters after we deleted so many rows anyway). We do this with the `set_index()` methode, in which we supply the name of the column to use as the new index. You should also set the `inplace` parameter to `True`.

```python
df.set_index('Name', inplace=True)
df.head()
```

**output**

| <br>Name | Date | Time (East Coast) | Launched? | Temp at Launch Time  Percipitation at Launch Time | Wind Speed at Launch Time | Visibility | Day Length | Condition |
|---|---|---|---|---|---|---|---|---|
| Pioneer 3 | 6-Dec-58 | 1:45 | Y | 62.00 | 0.00 | 11.00 | 10 | 10:25 | Cloudy |
| Pioneer 4 | 3-Mar-59 | 13:10 | Y | 78.00 | 0.00 | 12.00 | 7 | 11:38 | Cloudy |
| Ranger 1 | 23-Aug-61 | 11:04 | Y | 90.00 | 0.00 | 9.00 | 10 | 12:56 | Partly Cloudy |
| Ranger 2 | 18-Nov-61 | 9:09 | Y | 54.00 | 0.00 | 6.00 | 15 | 10:41 | Fair |
| Ranger 3 | 26-Jan-62 | 21:30 | Y | 53.00 | 0.00 | 17.00 | 10 | 10:45 | Fair |

Many of our column names are too long to conveniently work with. We can rename them using the DataFrame `rename()` method (again, using the `inplace=True` parameter).

```python
df.rename(columns={'Time (East Coast)': 'Time', 
                   'Launched?': 'Launched', 
                   'Temp at Launch Time': 'Temp',
                   'Percipitation at Launch Time': 'Percipitation', 
                   'Wind Speed at Launch Time': 'Wind Speed'},
          inplace=True)
df.head()
```

**output**

| <br>Name | Date | Time | Launched | Temp | Percipitation | Wind Speed | Visibility | Day Length | Condition |
|---|---|---|---|---|---|---|---|---|---|	
| Pioneer 3 | 6-Dec-58 | 1:45 | Y | 62.00 | 0.00 | 11.00 | 10 | 10:25 | Cloudy |
| Pioneer 4 | 3-Mar-59 | 13:10 | Y | 78.00 | 0.00 | 12.00 | 7 | 11:38 | Cloudy |
| Ranger 1 | 23-Aug-61 | 11:04 | Y | 90.00 | 0.00 | 9.00 | 10 | 12:56 | Partly Cloudy |
| Ranger 2 | 18-Nov-61 | 9:09 | Y | 54.00 | 0.00 | 6.00 | 15 | 10:41 | Fair |
| Ranger 3 | 26-Jan-62 | 21:30 | Y | 53.00 | 0.00 | 17.00 | 10 | 10:45 | Fair |

Take a quick check for any lingering `NaN` values in the DataFrame:

```python
df.isna().sum()
```

```output
Date             0
Time             1
Launched         0
Temp             0
Percipitation    0
Wind Speed       0
Visibility       0
Day Length       0
Condition        0
dtype: int64
```

We still have one last `NaN` in the `Time` column. Given that we don't have a subject-matter expert to consult on how important time of day might be to our model, we shouldn't drop the column. We also don't know how we might go about imputing a value to fill in that last `NaN`, so the best course is to remove the row with that missing value. 

Use the `dropna()` method to remove the row by setting the `how` parameter to `'any'`. You don't have to specify 'rows' or 'columns' to the method as removing rows is the default setting for the method.

```python
df.dropna(inplace=True, how='any')
df.isna().sum()
```

```output
Date             0
Time             0
Launched         0
Temp             0
Percipitation    0
Wind Speed       0
Visibility       0
Day Length       0
Condition        0
dtype: int64
```

Because you will be uploading this data to Azure (and as a general best practice to save your data after so much work!), export the DataFrame to a CSV file.

```python
df.to_csv('prepped_launch_data_raw.csv')
```