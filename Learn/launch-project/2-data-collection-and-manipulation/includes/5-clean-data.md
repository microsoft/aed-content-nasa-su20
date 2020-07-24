# Excerise - Clean Weather Data to Analyze Rocket Launch Criteria

We have to collect as much data as possible
 - AI and Machine Learning systems need data to learn, without data they cannot learn anything!
 Therefore we first have to collect as much as data about launches as possible. For this learning path we have collected and used Microsoft excel to store them, here is a screenshot of the data collected. 

 ```Python
## To handle missing values, we will fill the missing values with appropriate values 
lanch_data['Launched?'].fillna('N',inplace=True)
lanch_data['Crewed or Uncrewed'].fillna('Uncrewed',inplace=True)
lanch_data['Wind Direction'].fillna('unknown',inplace=True)
lanch_data['Condition'].fillna('Fair',inplace=True)
lanch_data.fillna(0,inplace=True)
lanch_data.head()
 ```

 ```Python
## As part of the data cleaning process we have to convert text data to numerical because computers only understand numbers
label_encoder = preprocessing.LabelEncoder()

# There are 3 columns that have categorical text info and we convert them to numbers
lanch_data['Crewed or Uncrewed'] = label_encoder.fit_transform(lanch_data['Crewed or Uncrewed'])
lanch_data['Wind Direction'] = label_encoder.fit_transform(lanch_data['Wind Direction'])
lanch_data['Condition'] = label_encoder.fit_transform(lanch_data['Condition'])
```

```Python
lanch_data.head()
```