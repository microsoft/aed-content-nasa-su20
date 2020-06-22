# Starting our Rock Classification Project

In this section we will be applying the basic concepts that we have learned about Python to create part of our desired project.

## Setting up program and variables

Let's begin by starting with a fresh slate. You can do this by either deleting everything in the file that you have been playing around in or by making a new Python file.

To start our program, we will want to let the user know that the program is beginning. To do this, we will use the print command to output a string of text.

```python
print("Artemis Rover Rock Scanner Starting")
```

Next, we are going to want to create some variables which are going to represent the different types of rocks that Artemis encountered on the Moon. The specific rocks that we are looking for are: Basalt: The Mare Rock, Breccia: Shocked Rock, Highland Rock: Anorthosite, and Regolith Soil/Surface Layer. Let's make some variables with names of "basalt", "breccia", "highland", and "regolith". We can also set these variables to 0 since we have not counted any rocks yet.

```python
basalt = 0
breccia = 0
highland = 0
regolith = 0
```

:::image type="content" source="Media\DeclareVariables.png" alt-text="test":::

## Loading in Libraries and text files

Start by downloading this file which represents the file that Artemis gave us with the different types of rocks viewed. Put this file in the same folder as where your Python file is saved.

Next, copy and paste the text below into the editor.

```python
strPath = "rocks.txt"
f = open(strPath)
line = f.readline()

while line:
    line = f.readline()
    print(line)
f.close()
```

Going through this code, we can see that the first line creates a string variable that is the same name as the text file that we just saved. The open command will then read the rock file that we have added and store it in a new variable. Next, we will use the readline function to read the data from this variable and store it in another variable named line.

Furthermore, we will use a loop to go through every line in the file until we reach the end and print the text that we see. This will set us up perfectly to call a function that will look at each word and add to our corresponding variables.

:::image type="content" source="Media\ReadingFile.png" alt-text="test":::

## Creating a function to classify the words

The next step in our application is to add a function that will look at a line of text and tell us which type of rock it is and then increment the corresponding variable. To start, we will paste the line:

```python
def countMoonRocks(s):

  if("basalt" in s):
    print("found a basalt\n")
    global basalt
    basalt += 1
    
  return
```

As you recall, these lines will create a function that has a parameter of variable "s" and does not return anything. We will be the one passing in the line to the function, so we know that the string going into the function will have one of five names: Basalt, Breccia, Highland, Regolith, and Unknown. To increment the correct variable based upon the types of rocks that Artemis encountered, we will use if statements.

Start by using the following line of code to check if the string we have passed through to the function is of type Basalt. If it is, we will go into the if statement and print out that we have found a Basalt rock and then increment the variable for Basalt by one.

:::image type="content" source="Media\AddFunction.png" alt-text="test":::

Do this for the remaining types of rocks.

## Adding a call to the function

Now that we have the function made, we will need to include a call to it so it will used. To do this, we will go into the while loop we have that reads each line of the text and prints it to the console. Instead of printing it to the console, let's call the function we just created. Paste the following line where the print statement was:

```python
countMoonRocks(line)
```

:::image type="content" source="Media\AddCallToFunction.png" alt-text="test":::

This will call the function that we have created every time that we discover a new rock. The function will then add up each type of rock to its respective variable. Now that we have all of the rock counts in their variables, we can use some additional code to write summaries about them.

## Analyzing summary data

Let's start by printing the number of each type of rock we found. For example, to do this for Basalt rocks, paste in the following code:

```python
print("Number of Basalt: ", Basalt)
```

As you can see, we first output a string telling the user what they are going to be seeing and then we concatenate on the variable name which includes the number of how many Basalt rocks we found.

Try this for the other four types of rock variables we created.

Next, let's provide some more general data like the type of rock that was the most and least common. To do this, we will use the max() and min() functions that we learned about before.

Try to figure this out and if you get stuck, read below for the answer:

```python
print("The rock that was found the most was: ", max(basalt, ))
print("The rock that was found the least was: ", min(basalt, ))
```

Congratulations, you have now successfully programmed Artemis to give a summary about the different types of rock data that it found.
