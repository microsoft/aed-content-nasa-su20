# Exercise - Import Python Libraries and Rocket Launch Data 

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

```Python
lanch_data = pd.read_excel('weather/RocketLaunchDataCompleted.xlsx')
# We will check out the first 5 rows of the data imported to make sure we have read them correctly
lanch_data.head()
```

```Python
# What are the columns available in our dataset
lanch_data.columns
```