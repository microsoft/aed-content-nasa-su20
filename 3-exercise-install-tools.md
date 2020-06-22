# Installing VS Code and the Python Extension

While it was great reading about VS Code and Python, a much more fun way to learn about them is to install them and begin playing around.

## Installing VS Code

As mentioned before, VS Code is free and available [here](https://code.visualstudio.com/Download). Simply click on the download box according to what OS you are running, then click on the grey box at the bottom left of the screen once it is done downloading.

> [!NOTE]
> The picture below depicts a user using a Windows computer, but you should choose the box that represents your system.

:::image type="content" source="Media\DownloadVSCode.png" alt-text="test":::

After clicking on the box, you will be asked to accept the license agreement and be asked where to install. Fill out these preferences and then finish the installation.

## Configuring VS Code

Once VS Code is installed, you may have the option to have it open on its own, however if you don't see this, just find the application on your computer and open it. When you first come into VS Code, you will be greeted with a welcome window. Let's start by closing this window. You will see on the left side of the screen that there are a variety of icons you can click on. Below is a brief overview of a few of the sections that we will be using.

:::image type="content" source="Media\WelcomeVSCode.png" alt-text="test":::

- Explorer: Shows what file(s) you have open and shows the contents of the folder you are in, if you are in one.
- Search: Allows you to look for a certain word or collection of words in your file
- Run: This button will run the code you have written
- Extensions: This is where you can see all of the additions that people from across the globe have added. There are different color themes, programming languages, and much more. You can install and customize VS Code to however you please.

## Installing Python Extension

To access all of the open-sourced-made tools we learned about, click on the extension tab. You can play around and install some extensions, but for this tutorial, we will be installing the Python Extension. After you are inside of the extension page, go to the search bar and type in "Python". You are looking for the extension named solely Python (it should be the first result). Simply click on the box and then click "install".

:::image type="content" source="Media\InstallPython.png" alt-text="test":::

## Installing Python on your computer

In the previous step, we installed software that will help us write Python, but we still have to install Python on our computer so it knows how to run the code we write. If you have a Mac, Python should already be installed. Any other OS will need to go to this [link](https://www.python.org/downloads/) to download. Do the same steps as you did to install VS Code to install Python. Click on the download button and then click the grey box at the bottom left of the screen and follow the directions for installation.

## Final Set Up and Testing

The last step is to tell VS Code where Python is installed and then you will finally get to see where all of your hard work has gone.

Go back to VS Code and locate the "file" tab at the top of the screen. Click on this to view a drop down menu and click on "new file". You will then be taken to a blank file. Now we are going to make this into a Python file, so click file and save or ctrl s. An optional step is to make a folder to easily organize all of the Python files you will create. Pick a location you want to save the file and change the file type to "Python" from the drop down extension. This will save your file to your computer and change the type of document to a Python file that we can code in.

:::image type="content" source="Media\MakePython.png" alt-text="Create Python File":::

Finally, on the bottom left of the screen, you will need to choose which Python environment you are using. Simply click the box and select the version of Python that you installed.

:::image type="content" source="Media\PythonEnvironment.png" alt-text="Set Python environment":::

Last, we will test if everything is set up correctly. Write print("Hello World") in the editor and click the play button on the top right of the screen. 

```python
print("Hello World")
```

Another window should pop up that reads output and you should see "Hello World" printed.   
Congratulations! You just programmed a computer to output text. Next step: ~~hacking the mainframe~~ creating our rock identifying program!
