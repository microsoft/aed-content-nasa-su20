# Exercise - Import Python Libraries and Rocket Launch Data 

Now that we know a little bit about what we want to accomplish, let's start creating the machine learning model. The first step is to import some libraries that will help us create the model and import the weather data.

Copy the following code into a cell and run it to import all of the needed libraries.

```Python
# Pandas library is used for handling tabular data
import pandas as pd
# Numpy is used for handling numerial series operations (addition, multiplification and ...)
import numpy as np
# Sklearn library contain all the machine learning packages we need to digest and extract patterns from the data
from sklearn import linear_model, model_selection, metrics
from sklearn.model_selection import train_test_split

# Machine learning libaries used to build a decision tree
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

# Sklearns preprocessing library is used for processing and cleaning the data 
from sklearn import preprocessing

# for vizualizing the tree
import pydotplus
from IPython.display import Image 
```

Now that we have all of the libraries imported, we can use the pandas library to import our data. Use the command `pd.read_excel` to read the data and save it in a variable. Then, we will use the `.head()` function to print out the first 5 rows of the data. This will ensure that we have read everything correctly.


```Python
lanch_data = pd.read_excel('../Media/weather/RocketLaunchDataCompleted.xlsx')
lanch_data.head()
```

Finally, we can use the `.columns` function call to view all of the columns in our data. This will show us the different attributes the data has. You will see some common attributes like names of past rockets that have been scheduled to launch, the data they were scheduled, if they actually launched, and many more. Look at these columns and try to guess which ones will have the greatest impact of determining if a rocket will launch or not.

```Python
lanch_data.columns
```
