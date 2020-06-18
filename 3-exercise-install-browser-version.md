# Running VS Code in your browser

One of the great things about VS Code is that Microsoft Azure gives you the opportunity to run the program in your browser. This means that you can learn about coding all without download anything.

## Create a Microsoft Azure Account

To start using this program in your browser you must first start out by making a free Microsoft Azure account. Start by going to this [link](https://ms.portal.azure.com/). Either sign in with a Microsoft account or create a free account.

## Instructions to set up Code spaces

To run the code in your browser we are going to be utilizing a Microsoft product named CodeSpaces. The concept of this is Microsoft downloaded the VS Code program on their computers and we are basically using their computer to run the program. A quick startup guide to get CodeSpaces working is found [here](https://docs.microsoft.com/en-us/visualstudio/online/quickstarts/browser).

> [!NOTE]
> Microsoft Codespaces does have a fee, however when creating a Microsoft Azure account you are given $200 credit. It should essentially be free.

## Configuring Code Spaces

Once you are connected to Code Spaces, you will be greeted with a welcome window. Let's start be closing this window. You will see on the left side of the screen there are a variety of icons you can click on. Below is a brief overview of a few of the sections that we will be using.

:::image type="content" source="Media\CodeSpaceStart.png" alt-text="test":::

- Explorer: Shows what file(s) you have open and shows the contents of the folder you are in, if you are in one.
- Search: Allows you to look for a certain word or collection of words in your file
- Run: This button will run the code you have written
- Extensions: This is where you can see all of the additions people from across the globe have added. There are different color themes, programming languages, and much more you can install and customize VS Code to however you please

## Installing Python Extension

To access all of the open sourced made tools we learned about click on the extension tab. You can play around and install some extensions, but for this tutorial we will be installing the Python Extension. After you are inside of the extension page, go to the search bar and type in "Python". You are looking for the extension named just Python (it should be the first result). Simply click on it and the click "install".

:::image type="content" source="Media\CodeSpacePython.png" alt-text="test":::

## Final Set Up and Testing everything out

The last step is to tell CodeSpaces where Python is installed and then you will finally get to see where all of your hard work went.

Go back to Code Spaces and locate the hamburger menu button the click the "file" tab at the top of the screen. Click on this to view a drop down menu and click on "new file". You will be taken to a blank file. Now we are going to make this into a python file, so click file and save or ctrl s. Pick a location you want to save the file and change the file name to be some title with a ".py" at the end of it. This will save your file and change the type of the document to a Python file that we can code in.

:::image type="content" source="Media\CodeSpaceCreateFile.png" alt-text="Create Python File":::

Finally, on the bottom left of the screen you will need to choose which Python environment you are using. Simply click the box and select the version of Python installed.

:::image type="content" source="Media\CodeSpacePythonEnvironment.png" alt-text="Set Python environment":::

Last we will test if everything is set up correct. Write print("Hello World") in the editor and click the play button on the top right of the screen. Another window should pop up that says output and you should see Hello World printed.

:::image type="content" source="Media\CodeSpaceHelloWorld.png" alt-text="Set Python environment":::

Congratulations! You just programmed a computer to output text. Next step ~~hacking the mainframe~~ creating our rock identifying program!
