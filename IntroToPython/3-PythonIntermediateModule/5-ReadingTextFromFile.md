# Importing Data with Python

In many applications of Python, you will need to use data that comes from some other source. This could come in the form of reading an Excel File with data tracking the various parts of a rocket or a text file to read the rocks that a moon rover sees. In this unit we will learn how to read data from a text file using a pre-made Python function.

## Setting up Data

The first step to reading data from a file is to first get a file and save it in a location that we can tell Python to access later. First, find out where your Jupyter notebook file is saved. This may be in a Python folder or even your desktop. Next, you will need to save the data file linked here. It is very important to save this file in the same location as your Jupyter Notebook file. This will make is very easy to tell Python where to find the data.

## Getting Data in Jupyter Notebook

Now that we have our data saved, we must make a string in Python telling us what the file name is.

```python
strPath = "text.txt"
```

Next, we will use the open() function to get the file in Python. We will make a new variable called f to hold the data.

```python
f = open(strPath)
```

Finally, we will have Python read this f variable to give us a string that we can actually use by using the read() function. We will store this in another variable so we can print it out later.

```python
strText = f.read()
```

Finally, we can print the contents of the string we just read by calling:

```python
print(strText)
```

The example above just teaches us how to get the full data into Python. After we have this data into Python we can begin to go through it and break it down line by line. This is called parsing in programming. To parse through the text we just imported, let's go line by line and print the lines out. To go line by line we will call a function called readline(). This function will just give us what is on the next line.

```python
firstLine = strText.readline()
```

This code will give us the first line of the text.

```python
strText.readline()
secondLine = strText.readline()
```

This code will read the first line, do nothing with it and then read the second line of the text and store it in a variable.
