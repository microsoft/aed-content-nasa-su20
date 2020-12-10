# Local Machine Learning: Data Preparation

Now that you've seen what you can do with Azure Machine Learning, let's see how it compares with doing machine learning locally using Python.

## Prepare DateTime Data

One big difference in doing machine learning locally is that you have to clean you data much more thoroughly. How thorough is thorough enough depends on the machine learning you want to do. As stated in the last section, we are trying to classify between days of likely versus unlikely launch-delay. In this case, we want to know the date that on-time and delayed occured, but less because we want to place them on a timeline (such as for prediction, perhaps), but so we can judge if some seasons of the year are more conducive to on-time rocket launches from the central east coast of Florida. As such, what we really care about is the day of the year rather than the date.

Before proceeding, let's check to see what datatypes are in each column. To do this, you can just loop over each column in the DataFrame and print out its name and datatype.

```python
for col in df:
    print(col, df[col].dtype)
```

```output
Date object
Time object
Launched object
Temp float64
Percipitation float64
Wind Speed float64
Visibility int64
Day Length object
Condition object
```

When pandas reports that a datatype is an object, it is refering to standard Python objects, one of which is the string type. So right now the `Date`, `Time`, `Day Length`, and `Condition` columns are all strings, none of which will work for our machine learning.

The first thing we have to do is convert the `Date` column to DateTime. Pandas DataFrames have a built-in method for doing this conversion (`to_datetime()`), but this won't fully do the job as we have a number of dates in this list from the 1960s. We also need to subtract 100 years off of any date that is after the current date. For that, use the Python `date` module from the `datetime` library.

`date.today()` supplies today's date and `strftime('%Y')` converts the date to a string and takes just the four-digit year. The `dt.year` method does the same for the `Date` column. Finally, the `DateOffset()` function lets us subtract 100 years from a date.

```python
from datetime import date

df['Date'] = pd.to_datetime(df['Date'], yearfirst=True)
df.loc[df['Date'].dt.year >= int(date.today().strftime('%Y')), 'Date'] -= pd.DateOffset(years=100)
df.head()
```

| <br>Name  | Date | Time | Launched | Temp | Percipitation | Wind Speed | Visibility | Day Length | Condition |
|---|---|---|---|---|---|---|---|---|---|									
| Pioneer 3 | 1958-12-06 | 1:45 | Y | 62.0 | 0.0 | 11.0 | 10 | 10:25 | Cloudy |
| Pioneer 4 | 1959-03-03 | 13:10 | Y | 78.0 | 0.0 | 12.0 | 7 | 11:38 | Cloudy |
| Ranger 1 | 1961-08-23 | 11:04 | Y | 90.0 | 0.0 | 9.0 | 10 | 12:56 | Partly Cloudy |
| Ranger 2 | 1961-11-18 | 9:09 | Y | 54.0 | 0.0 | 6.0 | 15 | 10:41 | Fair |
| Ranger 3 | 1962-01-26 | 21:30 | Y | 53.0 | 0.0 | 17.0 | 10 | 10:45 | Fair |

Now that we have to correct datesm, we need to convert the DateTime objects in the `Date` column (which scikit-learn can't use for classification) to an integer values. You can use the pandas `dt.dayofyear()` method to get this number. You should also rename the column to a more descriptive name, such as `Day of Year`.

```python
df['Date'] = df['Date'].dt.dayofyear
df.rename(columns={'Date': 'Day of Year'}, inplace=True)
df.head()
```

| <br>Name | Day of Year | Time | Launched | Temp | Percipitation | Wind Speed | Visibility | Day Length | Condition |
|---|---|---|---|---|---|---|---|---|---|							
| Pioneer 3 | 340 | 1:45 | Y | 62.0 | 0.0 | 11.0 | 10 | 10:25 | Cloudy |
| Pioneer 4 | 62 | 13:10 | Y | 78.0 | 0.0 | 12.0 | 7 | 11:38 | Cloudy |
| Ranger 1 | 235 | 11:04 | Y | 90.0 | 0.0 | 9.0 | 10 | 12:56 | Partly Cloudy |
| Ranger 2 | 322 | 9:09 | Y | 54.0 | 0.0 | 6.0 | 15 | 10:41 | Fair |
| Ranger 3 | 26 | 21:30 | Y | 53.0 | 0.0 | 17.0 | 10 | 10:45 | Fair |

We now need to do a similar transformation on the `Time` and `Day Length` columns. For those columns, we need an integer value that summarizes the what part of the day a launch-event occured (or how long that day is). Converting these from hour:minute format to number of minutes should work. However, the pandas method that makes sense for this (`to_timedelta`) requires hour:minute:second format, so we need to add `':00'` to all entries in those columns. A Python list comprehension is a convenient way to do this.

```python
df['Time'] = [str(x) + ':00' for x in list(df['Time'])]
df['Day Length'] = [str(x) + ':00' for x in list(df['Day Length'])]
df.head()
```

| <br>Name | Day of Year | Time | Launched | Temp | Percipitation | Wind Speed | Visibility | Day Length | Condition |
|---|---|---|---|---|---|---|---|---|---|								
| Pioneer 3 | 340 | 1:45:00 | Y | 62.00 | 0.00 | 11.00 | 10 | 10:25:00 | Cloudy |
| Pioneer 4 | 62 | 13:10:00 | Y | 78.00 | 0.00 | 12.00 | 7 | 11:38:00 | Cloudy |
| Ranger 1 | 235 | 11:04:00 | Y | 90.00 | 0.00 | 9.00 | 10 | 12:56:00 | Partly Cloudy |
| Ranger 2 | 322 | 9:09:00 | Y | 54.00 | 0.00 | 6.00 | 15 | 10:41:00 | Fair |
| Ranger 3 | 26 | 21:30:00 | Y | 53.00 | 0.00 | 17.00 | 10 | 10:45:00 | Fair |

Now that they are in the correct format, we can convert `Time` and `Day Length` to integers for use with scikit-learn.

```python
from datetime import time

df['Time'] = pd.to_timedelta(df['Time']).dt.total_seconds().div(60).astype(int)
df['Day Length'] = pd.to_timedelta(df['Day Length']).dt.total_seconds().div(60).astype(int)
df.head()
```

| <br>Name | Day of Year | Time | Launched | Temp | Percipitation | Wind Speed | Visibility | Day Length | Condition |
|---|---|---|---|---|---|---|---|---|---|										
| Pioneer 3 | 340 | 105 | Y | 62.00 | 0.00 | 11.00 | 10 | 625 | Cloudy |
| Pioneer 4 | 62 | 790 | Y | 78.00 | 0.00 | 12.00 | 7 | 698 | Cloudy |
| Ranger 1 | 235 | 664 | Y | 90.00 | 0.00 | 9.00 | 10 | 776 | Partly Cloudy |
| Ranger 2 | | 322 | 549 | Y | 54.00 | 0.00 | 6.00 | 15 | 641 | Fair |
| Ranger 3 | 26 | 1290 | Y | 53.00 | 0.00 | 17.00 | 10 | 645 | Fair |

We also need to address the string values in the `Launched` column. Scikit-learn will not be able to use these values for our model label, so we need to turn them in integer values (`1` for `Y` and `0` for `N`). Use the DataFrame `replace()` method to do this.

```python
df['Launched'] = df['Launched'].replace(to_replace=['N', 'Y'], value=[0, 1])
df.head()
```

| <br>Name | Day of Year | Time | Launched | Temp | Percipitation | Wind Speed | Visibility | Day Length | Condition |
|---|---|---|---|---|---|---|---|---|---|								
| Pioneer 3 | 340 | 105 | 1 | 62.00 | 0.00 | 11.00 | 10 | 625 | Cloudy |
| Pioneer 4 | 62 | 790 | 1 | 78.00 | 0.00 | 12.00 | 7 | 698 | Cloudy |
| Ranger 1 | 235 | 664 | 1 | 90.00 | 0.00 | 9.00 | 10 | 776 | Partly Cloudy |
| Ranger 2 | 322 | 549 | 1 | 54.00 | 0.00 | 6.00 | 15 | 641 | Fair |
| Ranger 3 | 26 | 1290 | 1 | 53.00 | 0.00 | 17.00 | 10 | 645 | Fair |

For reasons that will become clearer later on, now is a good time to make a backup of the DataFrame. (As a best practice, it is always good to backup your data anyway, particularly if you have done a lot of work to it.) Use the `copy()` method to do this; the `deep=False` parameter will ensure that it is only a shallow copy so that that any subsequent changes you make in the `df` DataFrame will not affect your backup.

```python
df_backup = df.copy(deep=False)
```

## Create Dummy Variables

The final column in the DataFrame with string values is `Condition`. We need to turn those values into integer values, but we have more than two possibilities for the weather conditions. In situations like this, we need to employ dummy variables.

Dummy variables take only the value 0 or 1 to indicate the absence or presence of a condition (such as 0 or 1 for Fair, 0 or 1 for Cloudy, etc.). Fortunatly, pandas has the `get_dummies()` method to do just this. Create a new DataFrame housing just the dummy variables derived from the `Condition` column.

```python
dummy = pd.get_dummies(df['Condition'])
dummy.head()
```

| <br>Name | Cloudy | Fair | Heavy T-Storm | Partly Cloudly | Partly Cloudy | Rain |
|---|---|---|---|---|---|---|						
| Pioneer 3 | 1 | 0 | 0 | 0 | 0 | 0 |
| Pioneer 4 | 1 | 0 | 0 | 0 | 0 | 0 |
| Ranger 1 | 0 | 0 | 0 | 0 | 1 | 0 |
| Ranger 2 | 0 | 1 | 0 | 0 | 0 | 0 |
| Ranger 3 | 0 | 1 | 0 | 0 | 0 | 0 |

Notice that there was a typo in the `Condition` column, and `get_dummies()` has thus created dummy variables for both `Partly Cloudy` and `Partly Cloudly`. Let's go back to the original DataFrame and clear that up before creating the dummy variables. To do so, you can use the DataFrame `replace()` method and then re-generate the dummy variables.

```python
df['Condition'] = df['Condition'].replace(to_replace=['Partly Cloudly'], value=['Partly Cloudy'])

dummy = pd.get_dummies(df['Condition'])
dummy.head()
```

| <br>Name | Cloudy | Fair | Heavy T-Storm | Partly Cloudy | Rain |
|---|---|---|---|---|---|						
| Pioneer 3 | 1 | 0 | 0 | 0 | 0 |
| Pioneer 4 | 1 | 0 | 0 | 0 | 0 |
| Ranger 1 | 0 | 0 | 0 | 1 | 0 |
| Ranger 2 | 0 | 1 | 0 | 0 | 0 |
| Ranger 3 | 0 | 1 | 0 | 0 | 0 |

Much better! Now we just have to concatenate the dummy variables with the original DataFrame. You can use the `concat()` function to do this. Note that you will only leave off the `Condition` column from the original DataFrame when you do this (its data is now encapsulated in the dummy variables). You will also need to use the `axis=1` parameter to tell pandas to concatenate the dummy variables as new columns rather than new rows.

```python
df = pd.concat([df.iloc[:, :-1], dummy], axis=1)
df.head()
```

| <br>Name | Day of Year | Time | Launched | Temp | Percipitation | Wind Speed | Visibility | Day Length | Cloudy | Fair | Heavy T-Storm | Partly Cloudy | Rain |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|													
| Pioneer 3 | 340 | 105 | 1 | 62.00 | 0.00 | 11.00 | 10 | 625 | 1 | 0 | 0 | 0 | 0 |
| Pioneer 4 | 62 | 790 | 1 | 78.00 | 0.00 | 12.00 | 7 | 698 | 1 | 0 | 0 | 0 | 0 |
| Ranger 1 | 235 | 664 | 1 | 90.00 | 0.00 | 9.00 | 10 | 776 | 0 | 0 | 0 | 1 | 0 |
| Ranger 2 | 322 | 549 | 1 | 54.00 | 0.00 | 6.00 | 15 | 641 | 0 | 1| 0 | 0 | 0 |
| Ranger 3 | 26 | 1290 | 1 | 53.00 | 0.00 | 17.00 | 10 | 645 | 0 | 1 | 0 | 0 | 0 |

As a final data-preparation step, let's move the `Launch` column to the end of the DataFrame as it will serve as the label for the machine-learning models we will build. There is no slick built-in way to do this, so one way to move a column if there are more than you want to manually type out is to create a list of the column names, manipulate the order of column names in that list, and then reorder the DataFrame columns according to that list.

```python
column_list = list(df)

launched = column_list.pop(2)
column_list.append(launched)

df = df[column_list]
df.head()
```

| <br>Name | Day of Year | Time | Temp | Percipitation | Wind Speed | Visibility | Day Length | Cloudy | Fair | Heavy T-Storm | Partly Cloudy | Rain | Launched |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|														
| Pioneer 3 | 340 | 105 | 62.00 | 0.00 | 11.00 | 10 | 625 | 1 | 0 | 0 | 0 | 0 | 1 |
| Pioneer 4 | 62 | 790 | 78.00 | 0.00 | 12.00 | 7 | 698 | 1 | 0 | 0 | 0 | 0 | 1 |
| Ranger 1 | 235 | 664 | 90.00 | 0.00 | 9.00 | 10 | 776 | 0 | 0 | 0 | 1 | 0 | 1 |
| Ranger 2 | 322 | 549 | 54.00 | 0.00 | 6.00 | 15 | 641 | 0 | 1 | 0 | 0 | 0 | 1 |
| Ranger 3 | 26 | 1290 | 53.00 | 0.00 | 17.00 | 10 | 645 | 0 | 1 | 0 | 0 | 0 | 1 |

We're now ready to tackle machine learning on this data in the subsequent modules.