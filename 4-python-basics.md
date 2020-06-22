# Python Basics

Now that we have Python running in VS Code, we can now proceed to learn how to use these tools to complete our Moon rock mission.

## Arithmetic

Similar to a calculator you, can use the operators + , - , * , and / in Python.

For example, write the following in the editor and then click the run button to see the output.

```python
print(2 + 2)
```

```python
print(15 - 3)
```

```python
print(5 * 2)
```

```python
print(10 / 5)
```

Furthermore, just like on calculators, the order of operations is in play and you can use parenthesis to combat this.

```python
 2 + 5 * 3
(2 + 5) * 3
```

There are also more advanced calculations that Python can compute listed below:

- To calculate remainder, use %

```python
10 % 4
```

- To calculate exponents, use **

```python
2 ** 3
```

- To remove the remainder when dividing, use //

```python
5 // 2
```

## Comments

Comments are lines in your code that are ignored when you run the program. They are used to explain code to others who may read it or for you to remember what something does or a reminder to complete something.

To write a comment in Python, simply add a # in front of the line.

```python
# This is a comment
```

Usually you will want to use it to describe the lines below it:

```python
# Add 5 and 10
5 + 10
```

## Variables

Variables are basically containers that you can store data within and use at a different time.

There are four main data types:

- Integers (int): These are whole numbers like 1,4,10
- Floats: These are decimal numbers like 0.3, 1.6, 17.4
- String: These are chains of characters which are surrounded by single or double quotes like "hi", "goodbye", "start"
- Boolean: Represents either True or False

To tell the computer you want to make a variable (initialize), start by choosing any name of your choice and then use "=" to give it a value.

Try copying the code below to make some of your own variables:

```python
# Integer Variable
integerVar = 5

# Float Variable
floatVar = 1.1

# String Variable
stringVar = "Artemis Rover"

# Boolean Variable
booleanVar = False

```

An aspect of Python that makes it unique to other programming languages is that you do not need to tell it what type of variable you are making. For example in some languages if you want to make an integer in some languages you must let the computer know you are about to make an integer.
(int intVar = 0)

In our project, we will be using variables to store the number of a certain type of rock we find. One of the main types of moon rock is called Basalt. We can make a variable named basalt and give it a value of 0 by using the following code:

```python
# Make an integer variable named Basalt with value 0
basalt = 0
```

We can also change the value in the variable:

```python
basalt = 3
basalt = basalt + 1
```

There are so many things that we can do with strings and variables.

## Output

Now that we have made some variables and have given them some values we may want to see what the values are. To do this we will use a command called print(). This is called a function (you will learn more about functions in the next section) which is code others have wrote that we can use. The print() function will make the computer write the values in you variables to the screen.

Try to print some values to the console by using the code below:

```python
print(6)
print("Hello World")
```

Along with only values, we can use the code below to print a variable.

```python
numRocks = 15
print(numRocks)
```

Finally, we can combine variables and strings by using the following code:

```python
numBasalt = 4
print("The number of Basalt rocks found:", numBasalt)
```

This knowledge will be very helpful to output the rock data we find so others can more easily see the data we find.
