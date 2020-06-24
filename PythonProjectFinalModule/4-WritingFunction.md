# Creating a function to classify the words

The next step in our application is to add a function that will look at a line of text and tell us which type of rock it is and then increment the corresponding variable. To start, we will paste the line:

```python
def countMoonRocks(s):

  if("basalt" in s):
    print("found a basalt\n")
    global basalt
    basalt += 1
    
  return
```

As you recall, these lines will create a function that has a parameter of a string variable "s" and does not return anything. We will be calling the function and passing in a rock name that will have one of four: Basalt, Breccia, Highland, or Regolith. To ensure that the variables will remember how many rocks they have counted, we will need to make each rock type a global variable. To increment the correct variable based upon the types of rocks that Artemis encountered, we will use if statements.

Start by using the following line of code to check if the string we have passed through to the function is of type Basalt. If it is, we will go into the if statement and print out that we have found a Basalt rock and then increment the variable for Basalt by one.

Do this for the remaining types of rocks.
