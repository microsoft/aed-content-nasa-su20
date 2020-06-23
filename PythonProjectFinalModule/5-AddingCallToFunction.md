# Adding a call to the function

Now that we have the function made, we will need to include a call to it so it will used. To do this, we will go into the while loop we have that reads each line of the text and prints it to the console. Instead of printing it to the console, let's call the function we just created. Paste the following line where the print statement was:

```python
countMoonRocks(line)
```

:::image type="content" source="Media\AddCallToFunction.png" alt-text="test":::

This will call the function that we have created every time that we discover a new rock. The function will then add up each type of rock to its respective variable. Now that we have all of the rock counts in their variables, we can use some additional code to write summaries about them.
