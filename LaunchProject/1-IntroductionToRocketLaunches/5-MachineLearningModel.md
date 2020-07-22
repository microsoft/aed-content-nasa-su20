# Introducing Machine Learning

At this point in the data science lifecyle you have data that best represents the truth about what you are researching. So it's time to model the machine learning to start uncovering knowledge. Modeling is the process of choosing what features of the data (sometimes these are columns in a table, sometimes this is secondary information like the difference between two columns, and sometimes this is more nuanced like the color of an image) are the most likely drivers of knowledge. 

## Step 4: Modeling

Let's revisit the lettuce garden. As you explored in the last unit, there are some aspects of the lettuce's environment that are likely to be more important than others (e.g. soil moisture over noise level). But there are some features that are hard to determine which are more correlated with the desired outcome (e.g. is soil moisture more of an indicator of growth over time than temperature?). Featurization is a technique that allows us to choose the features we want to focus on, and then the machine learning model helps us understand what features are more tightly correlated with our outcomes. 

In the case of rocket launches, as previously mentioned, we aren't likely to even have the data that most correlated with our desired outcome (e.g. the shape, size, and classification of clouds), but we will have three main pieces of data that are likely to be most correlated (temperature, percipitation, and humidity). In this learning path, our goal is to use previous launch and weather data to determine if a launch is likely to be successful in the future using predicted weather data. This type of analysis uses a two-class classification algorithm because we are asking the yes or no question: Will this day, with these weather conditions, yield a successful launch?. 

## The Algorithm Cheat Sheet

A great resource for determining what kind of machine learning algorithm will be useful for your particular analysis is the [Algorithm Cheatsheet](https://docs.microsoft.com/en-us/azure/machine-learning/algorithm-cheat-sheet). 

![Algorithm Cheatsheet](LaunchProject\images\algorithmcheatsheet.jpg)

Let's revisit the question we're trying to answer with Launches:  
Will this day, with these weather conditions, yield a successful launch?   
This is a yes or no question, so this is a problem where a two-class classification algorithm can be helpful. You can see on the algorithm cheatsheet that within that category, there are many specific algorithms to choose from. In this case, we're choosing to use a decision tree classifier, which takes observations about an event (all of the weather conditions for a particular day) and draws conclusions about the target value (yes or no that a rocket would successfully launch that day). 

## Training and Testing the Model

With a machine learning algorithm chosen, it's time to train and test our specific model. In this case, the goal is to run our existing data through the algorithm keeping, which will learn what aspects of the data leads to what results. 