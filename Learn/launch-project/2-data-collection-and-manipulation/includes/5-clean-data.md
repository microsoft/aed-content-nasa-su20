# Excerise - Clean Weather Data to Analyze Rocket Launch Criteria

Now that we have the data imported, will we need to apply a machine learning practice known as "cleaning the data". This pretty much means what you think it means: take data that looks incorrect or messy and clean it up by changing the value or deleting it altogether. Some common examples of cleaning data are ensuring that there are no null values or making every value in a column look the same. 

We do this because computers will get confused if they look at inconsistent data or if lots of values in the data are null.

 - AI and Machine Learning systems need data to learn, without data they cannot learn anything!
 Therefore we first have to collect as much as data about launches as possible. For this learning path we have collected and used Microsoft excel to store them, here is a screenshot of the data collected. 

The first step that we will take to clean our data is to replaces all the missing values with something. Replacing these values usually requires your best judgement because you might now know what the data should be. In our case, we have some blank values where we are missing some weather data. To not mess with our real data that much, we will replace this missing data with weather for a normal day (ie fair weather).

 ```Python
## To handle missing values, we will fill the missing values with appropriate values 
lanch_data['Launched?'].fillna('N',inplace=True)
lanch_data['Crewed or Uncrewed'].fillna('Uncrewed',inplace=True)
lanch_data['Wind Direction'].fillna('unknown',inplace=True)
lanch_data['Condition'].fillna('Fair',inplace=True)
lanch_data.fillna(0,inplace=True)
lanch_data.head()
 ```

Next, since computers only know how to read numbers, we will convert the text into numbers. As an example, we will use a "1" if a rocket is crewed and a "0" if a rocket is uncrewed.

 ```Python
## As part of the data cleaning process we have to convert text data to numerical because computers only understand numbers
label_encoder = preprocessing.LabelEncoder()

# There are 3 columns that have categorical text info and we convert them to numbers
lanch_data['Crewed or Uncrewed'] = label_encoder.fit_transform(lanch_data['Crewed or Uncrewed'])
lanch_data['Wind Direction'] = label_encoder.fit_transform(lanch_data['Wind Direction'])
lanch_data['Condition'] = label_encoder.fit_transform(lanch_data['Condition'])
```

Now let's look at all the data again after it has been cleaned. Looking all nice and fresh!

```Python
lanch_data.head()
```