# If-Statement

If statements are the actual programming we use to tell the computer if some condition is met, do this.

Some real world examples are:

- If the temperature is above freezing, the rocket will launch
- If oxygen level drop, grab a space suit and oxygen tank

In Python the format for an if statement is:

if(condition is true):
    do something

It is crucial to include the colon and include a tab on the line where you are telling the computer to do something.

Below is an example of an if statement in Python. We first check is the count of Basalt rocks is 0 and if it is print the statement. If the count of rocks is not 0, nothing will be done

```python
if(basalt == 0):
    print("we have found no basalt rocks")
```

## Else-Statement

Another import Conditionals topic are else statements. Else statements need to be after an if-statement and the program will always execute what is inside of the else statement if the condition in the if statement is not met.

```python
if(basalt == 0):
    print("we have found no basalt rocks")
else:
    print("we found some basalt rocks)
```

## ElseIf

The final concept in conditionals is the else-if statement. This is written after if-statement and before else statements. The else if statement is just another if statement that will check if its conditions are met after the first if-statement's conditions are not met.

```python
if(basalt == 0):
    print("found no basalt rocks")
elif(basalt == 1):
    print("found 1 basalt rock")
else:
    print("found more than 1 basalt rock)
```
