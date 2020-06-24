# Setting up program and variables

To start creating this program make a folder somewhere on your computer that you will be able to easily access. You can call is something like SpaceRockProject. After this is created, save the rocks.txt file in this folder. This file has all of the data about that rocks that we are going to be reading in Python.

Next, open Visual Studio code and click file then new file. Once the blank file is open, click ctrl s to save it. Navigate to the folder you just created, name the file something informative like ArtemisRockClassifier and change the file type to Jupyter from the drop down menu. Now that we have everything created, we can start coding!

To start our program, we will want to let the user know that the program is beginning. To do this, we will use the print command to output a string of text.

```python
print("Artemis Rover Rock Scanner Starting")
```

Next, we are going to want to create some variables which are going to represent the different types of rocks that Artemis encountered on the Moon. The specific rocks that we are looking for are: Basalt: The Mare Rock, Breccia: Shocked Rock, Highland Rock: Anorthosite, and Regolith Soil/Surface Layer. These are the four main types of rocks found on the moon. Let's make some variables with names of "basalt", "breccia", "highland", and "regolith". We can also set these variables to 0 since we have not counted any rocks yet.

```python
basalt = 0
breccia = 0
highland = 0
regolith = 0
```
