# Python Intermediate

Now that you have been introduced to some basic concepts of Python and computer science, we will now add a little spice that comes in the form of logic.

## Conditionals

Many times when programming we only want to perform a certain action when a certain condition is met. For example if we see a Basalt rock, we will want to add 1 to our Basalt variable.

### Conditions

Conditions are what needs to be met before we do a certain task. We can use logical operators to compare two values. The logical operators will then return either a True or a False value (boolean).

Below are some common logical operator:

- Equals: x == y
- Not Equals: x!=y
- Less than: x < y
- Less than or equal to: x <= y
- Greater than: x > y
- Greater than or equal: x >= y

### If-Statement

If statements are the actual programming we use to tell the computer if something is met, do this.

Some real world examples are:

- If it is Monday, I will go to school
- If it is below 50 degrees, I will wear a jacket

In Python the format for an if statement is:

if(condition is true):
    do something

It is crucial to include the colon and include a tab on the line where you are telling the computer to do something.
Below is an example of an if statement in Python. We first check is the count of Basalt rocks is 0 and if it is print the statement. If the count of rocks is not 0, nothing will be done

```python
if(basalt == 0):
    print("we have found no basalt rocks")
```

### Else-Statement

Another import Conditionals topic are else statements. Else statements need to be after an if-statement and the program will always execute what is inside of the else statement if the condition in the if statement is not met.

```python
if(basalt == 0):
    print("we have found no basalt rocks")
else:
    print("we found some basalt rocks)
```

### ElseIf

The final concept in conditionals is the else-if statement. This is written after if-statement and before else statements. The else if statement is just another if statement that will check if its conditions are met after the first if-statement's conditions are not met.

```python
if(basalt == 0):
    print("found no basalt rocks")
elif(basalt == 1):
    print("found 1 basalt rock")
else:
    print("found more than 1 basalt rock)
```

## Iterations

### While Loop

The while loop will keep doing an action until a certain condition is met. In the real world, we could see an example that is

### For Loop

The for loops is a cleaner version of the while loop. 

## Functions

Functions are ways that we can make our code cleaner, easier to work with, and less redundant. This could be applied to our example whereby instead of making an if statement to check the type of every single space rock, we can just give a function the space rocks and it can run the same code to check which type of rock it is each time.

To make a function in Python, we must first define it. We can do this by writing the code below

```python
def NameOfFunction():

  return
```

We always need to include the return work at the bottom of a function to tell Python that the function is over.

Furthermore, there is a concept in programming known as scope. This means different parts of code can only see certain variables.

```python
def countRocks():
    print(basalt)
  return

basalt = 1
```

Since the variable basalt is not made in the countRocks function, the function does not know this variable exists. Another way we can say this is basalt is out of the scope of the countRocks function.

To combat this, we can do two things:

- Make the variable a global variable that can be seen by everything in the program

```python
basalt = 1

def countRocks():
    global basalt
    print(basalt)
  return
```

- Let the function know that a variable exists

```python
def countRocks(basalt):
    print(basalt)
  return

basalt = 1
```

Along with functions that we write, Python also has functions written by others. For example, in our project, we will be using two pre-made functions called max() and min(). Now we could have written lots of if statements to determine what the maximum number out of a certain set of numbers would have been, or we can just call max() and input the numbers that we want to compare. The function max() would then give us the number that has the greatest value from within the list that we provided.

```python
max(1, 50, 100, 2)
```

The output of this would be 100 since it is the largest number.

You can also pass variables into this function and see which of them has the greatest value.

```python
max()
```
