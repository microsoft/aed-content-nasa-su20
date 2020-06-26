# Variables

In this unit, you will learn about variables in Python. Variables are containers that you can store data within and use at a different time.

There are four main data types variables can be:

- Integers (int): These are whole numbers like 1,4,10
- Floats: These are decimal numbers like 0.3, 1.6, 17.4
- String: These are chains of characters which are surrounded by single or double quotes like "hi", "NASA", "Space Rocks"
- Boolean: Represents either True or False

Try copying the code below and clicking the run button to make some of your own variables:

```python
# Integer Variable
numberOfRocks = 5

# Float Variable
tempInSpace = -457.87

# String Variable
roverName = "Artemis Rover"

# Boolean Variable
rocketOn = False

```

You can then look at the values in your variables by simply writing the variables name and clicking the run button (After you have created them).

```python
roverName
```

>'Artemis Rover'

An aspect of Python that makes it unique to other programming languages is that you do not need to tell it what type of variable you are making. For example in some languages if you want to make an integer you must let the computer know you are about to make an integer.
(int intVar = 0)

In our project later, we will be using variables to store the number of a certain type of rock we find. One of the main types of moon rock is called Basalt. We can make a variable named basalt and give it a value of 0 by using the following code:

```python
# Create integer variable named basaltRock with value 0
basaltRock = 0
```

We can also change the value in the variable:

```python
basalt = 3
basalt = basalt + 1
basalt
```

>4

This would be good if we wanted to tell the computer we have three rocks found so far and we just found another.

An easy way to perform an operation on a variable is to use the operation you want to apply and then an equal sign after it. This will perform the action and set the variable to the new value without actually needing to set it to the new value. FOr example:

```python
basalt = 5
basalt += 3 #Add 3
basalt -= 2 #Remove 2
```

Finally, you can use all of the arithmetic examples we used from the last unit on variables.

```python
# Find out how many miles until rocket reaches moon
distanceToMoon = 238855
distanceTraveled = 10234
distanceToMoon - distanceTraveled
```

>228621
