# Downloading and reading text files

Start by downloading this file which represents the file that Artemis gave us with the different types of rocks viewed. Put this file in the same folder as where your Python file is saved.

Next, copy and paste the text below into the editor.

```python
strPath = "rocks.txt"
f = open(strPath)
line = f.readline()

while line:
    line = f.readline()
    print(line)
f.close()
```

Going through this code, we can see that the first line creates a string variable that is the same name as the text file that we just saved. The open command will then read the rock file that we have added and store it in a new variable. Next, we will use the readline function to read the data from this variable and store it in another variable named line.

Furthermore, we will use a loop to go through every line in the file until we reach the end and print the text that we see. This will set us up perfectly to call a function that will look at each word and add to our corresponding variables.

:::image type="content" source="Media\ReadingFile.png" alt-text="test":::
