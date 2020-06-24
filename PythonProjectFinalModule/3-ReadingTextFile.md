# Downloading and reading text files

Now that we have some variables made, we will want to start giving these variables values. We want to count the number of times that we see a certain type of rock in the rock.txt file and save that number in the corresponding variable. For example, if there are 12 basalt rocks that Artemis read in the text file, then we will want the basalt variable to be set to 12.

Let's start by telling the computer to read in the rocks.txt file. To do this copy the code below.

```python
strPath = "rocks.txt"
f = open(strPath)
line = f.readline()
```

Going through this code, we can see that the first line creates a string variable that is the same name as the text file that we just saved. The open command will then read the rock file that we have added and store it in a new variable. This variable named f is not in a string format so we will use the readline function to read the data from this variable and store it in a string variable named line.

Now that we have a large string of text in the line variable, we will use a while loop to read through every line in the text. Each line represents a type of rock, so we will read each rock (line) and start by printing each one. Finally, we will call f.close() to tell Python we are done reading the file.

```python
while line:
    line = f.readline()
    print(line)
f.close()
```

While currently, we are only print out each rock that we see in a file, this will set us up perfectly to call a function. This function will look at each rock and add to the corresponding variable if it sees a rock of the correct type.
