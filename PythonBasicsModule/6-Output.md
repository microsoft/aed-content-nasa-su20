# Output

Now that we have made some variables and have given them some values we will learn of some other ways to view them. To do this we will use a function called print(). Jupyter Notebooks is very nice because it does not require us to type to print command to see an output, but in normal Python files, you must add print. Additionally, if you do not use the print function, Jupyter notebooks will only print out the final code. For example only 8 (5 + 3) is printed out:

```python
2 + 2
5 + 3
```

>8

The print function, like the functions we called for the strings, is code others have wrote that we can use. The print() function will make the computer write the values in you variables to the screen.

Try to print some values to the console by using the code below:

```python
print(6)
print("Hello World")
```

>6  
>Hello World

Along with only values, we can use the code below to print a variable.

```python
numRocks = 15
print(numRocks)
```

>15

We can combine variables and strings by putting a comma in between them:

```python
numBasalt = 4
print("The number of Basalt rocks found:", numBasalt)
```

>The number of Basalt rocks found: 4

```python
date = "February 26"
numRocks = 15
print("On", date, "number of rocks found:", numRocks)
```

>On February 26 number of rocks found: 15

The print function is very helpful because the people using our programs won't always be able see our code or not know how to read our code. The print function allows us to only show them the data we want them to see.
