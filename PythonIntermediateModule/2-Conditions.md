# Conditionals and Conditions

In the real world, we sometimes will only perform some action if a certain condition is met. This is the gist of conditionals and conditions in Computer Science. For example if we see a Basalt rock, we will want to add 1 to our Basalt variable. Lets start by learning about the different conditions we can check so we can decide whether to perform an action or not.

## Conditions

Conditions are what needs to be met before we do a certain task. We finding if a condition is met by comparing two values and to do this we use a term called logical operators. Logical operators will then return either a True, if the statement is true, or a False, if the statement is false, value (boolean).

For example if our condition is to check if the temperature is above freezing (to see if a rocket launch would be delayed) our condition would be temperature > 32. This would give us true if the temperature is above freezing and false if the temperature is freezing or below freezing.

Below are some common logical operator:

- Equals: x == y
- Not Equals: x!=y
- Less than: x < y
- Less than or equal to: x <= y
- Greater than: x > y
- Greater than or equal: x >= y

Try to play around with some logical operators in Jupyter Notebooks. Notice how the single equal sign and double equal signs have very different meanings. The single equal assigns a value to a variable while the double equals compares values. This is a common mistake beginner programmers often face.

```python
temp = 50
temp >= 32
temp < 32
```

You can also use these operators on other variable types.

```python
rock = "basalt"
"basalt" == rock
"highland" == rock
```

For reasoning that is beyond this module, sometimes when comparing variables, you must use commands like "in". This just checks if a word is inside of the variable.

```python
rock = "basalt"
"basalt" in rock
"highland" in rock
```

After we know how to write the conditions for if we want an action to execute or not, we can begin actually specifying what action we want to occur.
