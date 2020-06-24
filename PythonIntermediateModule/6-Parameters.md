# Scope of Functions and Parameters

Another interesting aspect of functions is that they cannot see variables that are inside of the function can not be used outside of it. For example this code would fail because we create the rocketNumber variable in the function and then try to use it outside of the function. Python does not know about that variable outside of the function so it will produce an error.

```python
def OutputRocketText():
    rocketNumber = 1
    print("Rocket will launch soon!")

    return

OutputRocketText()
print(rocketNumber)

```

Along with this if you have variables created outside of a function, you can access them inside of a function, but you can not change them.

```python
def OutputRocketText():
    rocketText = rocketText + "two days"

    return

rocketText = "We will launch in"
OutputRocketText()
```

As you can see this produces an error as well because we are trying to modify a variable that was created outside of a function.

To combat this we can do one of two thing:

- Make a variable a global variable
- Give a variable to the function, so it knows that the variable is

The easiest way to change the value of a variable inside of a function is to make is a global. A global variable means that everything in the program can modify it even if it modified inside of a function. To make something a global variable, you must make a variable before you call the function and then include a line in your function that says global variable name:

```python
def OutputRocketText():
    global rocketText
    rocketText = rocketText + " two days"

    return

rocketText = "We will launch in"
OutputRocketText()
print(rocketText)
```

The next way to modify variables inside of a function is to use something called parameters. Parameters are when you give a function knowledge of a variable when you call it. To tell Python you want your functions to have parameters use the following code:

```python
def OutputRocketText(text):

    text = text + " two days"

    return text

rocketText = "We will launch in"
newRocketText = OutputRocketText(rocketText)
newRocketText
```
