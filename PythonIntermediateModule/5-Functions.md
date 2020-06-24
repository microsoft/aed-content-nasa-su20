# Functions

Functions are ways that we can make our code cleaner, easier to work with, and less redundant.This could be applied to our example whereby instead of making an if statement to check the type of every single space rock, we can just give a function the space rocks and it can run the same code to check which type of rock it is each time. You probably have already seen some pre-made functions that you can call from your own code, but we will now learn how to write our own.

To make a function in Python, we must first tell python that it is a function. We use the word def to tell or define Python the following code is a function. You must then include a name for your function, parenthesis, and a colon. Finally, at the end of your function you must include the word return key word. This tells Python the function is done and return to the point where you called the function.

```python
def NameOfFunction():

  return
```

Notice how there are some spaces before the return statement? An aspect of Python is that is makes us of whitespace to act as the body of the function. Therefore, you must write things tabbed in from the side.

Now let's try to play around with an example of making our own functions.

```python
def OutputRocketText():

    print("Rocket will be launching soon!")

    return

OutputRocketText()
```

As you can see in the code, we start by defining a function that prints is a rocket is launching. Then we proceed to put code below it that will call the function. If we had multiple rocket launches instead of typing out the whole print line, we could just call the OutputRocketText function. This would make our code much cleaner and less redundant.
