# Starting our Rock Classification Project

In this section we will be applying the basic concepts we learned about Python to create part of our desired project.

## Setting up program and variables

To start our program we will want to let the user know that the program is starting. To do this we will use the print command to output a string of text.

```python
print("Artemis Rover Rock Scanner Starting")
```

Next, we are going to want to create some variables which are going to represent rocks. The rocks that we are looking for on the moon are: Basalt: The Mare Rock, Breccia: Shocked Rock,Highland Rock: Anorthosite, and Regolith Soil/Surface Layer. Let's make some variables with names of basalt, breccia, highland, regolith and unknown. We can also set these variables to 0 since we have not counted any rocks yet.

```python
basalt, breccia, shocked, highland = 0
```

## Loading in Libraries and text files

Start by downloading this file that represents the file Artemis gave us with the different rocks it viewed. Put this file in the same folder where your Python file is saved. 

Next, copy the text below into the editor.

```python
strPath = "rocks.txt"
f = open(strPath)
line = f.readline()

while line:
    line = f.readline()
    print(line)
f.close()
```

Going through this code we see that the first line makes a string variable that is the same name as the text file that we just saved. The open command will read the rock file we added and store it in a variable. Next, we will use the readline function to read the data from the variable and store this in another variable named line.

Furthermore, we will use a loop to go through every line in the file until we reach the end and print the text we see. This will set us up perfectly to call a function that will look at each word and add to our variables.

## Creating a function to classify the words

The next step in our application is to add a function that will look at a line of text and tell us what type of rock it is and then increment the right variable. To start, we will paste the line:

```python
def countMoonRocks(s):

  return 
```
As you recall these lines will create a function that has a parameter of variable s and does not return anything. We will be passing in the line to the function so we know that the string we get in the function will have one of five names: Basalt, Breccia, Highland, Regolith, and Unknown. To increment the right variable when we see a rock, we will us if statements. 

Start by using the following line to check if the string we passed to the function is of type Basalt. If it is, we will go into the if statement and print out that we have found a Basalt and then increment the variable for Basalt by one.

```python
if("Basalt" in s):
      print("found a Basalt\n")
      Basalt ++
```

Do this for the other potential types of rocks.

## Adding a call to the function

Now that we have the function made, we need to include a call to it so it gets used. To do this we will go into the while loop we have the reads each line of the text and prints it out to the console. Instead of printing it out to the console, let's call the function we just created. Paste in the line where the print statement was:

```python
countMoonRocks(line)
```

This will call the function every time we see a new rock. The function will then add up each type of rock in their specific variable. Now that we have all of the rock counts in the variables, we can use some more code to write summaries about them.

## Summary data about the rocks

Let's start by printing the number of each type of rock we found. To do this for Basalt paste in the following code:

```python
print("Number of Basalt: ", Basalt)
```

As you can see we first output a string telling the user what they are going to be seeing and then we concatenate on the variable name which has a number of how many Basalt rocks we found.

Try this for the other four types of variables/rocks we created.

Next, let's give some more general data like the rock that was found the most and the rock that was found the least. To do this we will use the max() and min() functions. 

Try to figure this out and if you get stuck read below for the answer:

```python
print("The rock that was found the most was: ", max(basalt, ))
print("The rock that was found the least was: ", min(basalt, ))
```

Congratulations, you have successfully programmed Artemis to give a summary about the different type of rock data that it finds. 