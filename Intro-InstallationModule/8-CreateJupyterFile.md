# Creating a Jupyter Notebook File and Running a Simple Program

Now that we have installed everything that we need, we can create our own Jupyter Notebook file and start coding.

## Creating a Jupyter Notebook File

To create a Jupyter Notebook file that will run our Python code go to VS Code and locate the "file" tab at the top left of the screen. Click on this to view a drop down menu and click on "new file". You will then be taken to a blank file. Now we are going to make this into a Jupyter file, so click file and save or ctrl s. An optional step is to make a folder to easily organize all of the Jupyter files you will create. Name your file anything you please, pick a location you want to save the file, and change the file type to "Jupyter" from the drop down menu. This will save the file to your computer and change the type of document to a Jupyter Notebook file that we can code in. You will know it worked if in the top left of the screen you see the name you gave to the file followed by ".ipynb".

:::image type="content" source="Media\MakeJupyter.png" alt-text="Set Python environment":::

## Configuring Python Environment

Once the file changes to Jupyter Notebook, on the bottom left of the window, you will need to choose which Python environment you are using. After you installed Python, VS Code might already recognize Python, but if it doesn't simply click the box on the bottom left of the screen and select the version of Python that you installed.

Next, you will need to add Jupyter notebooks to the path. To do this click the green play button. Then at the bottom right of the screen you will see a pop-up asking you to install Jupyter Notebooks, click install and it will begin to install.

:::image type="content" source="Media\InstallJupyter.png" alt-text="Set Python environment":::

Now Jupyter Notebooks should be installed to your computer. You may need to select the environment again at the top right of the window as well. Choosing the environment tells VS Code what version of Python you installed and where VS Code can find it.

:::image type="content" source="Media\JupyterEnvironment.png" alt-text="Set Python environment":::

## Information about Jupyter Notebooks

In Jupyter notebooks, there will be cells that you can type code in. The plus button to the left of a cell will create a new cell when you click on it and the garbage can to the right of it will delete the selected cell. Additionally, the green play button in each cell will run that cell. After you run a cell, a number will appear surround by square brackets. This helps you keep track of what cells you just ran. Looking at the top of the file, you can choose to run all cells above or below the current cell with the play button and an up or down arrow. Finally, you can click the red pause button to force stop the program.

## Writing and Running Simple Program

Last, we will test if everything is set up correctly. Write "Hello World" in the the first line of the editor and click the green play button.

```python
"Hello World"
```

:::image type="content" source="Media\RunJupyter.png" alt-text="Run Jupyter":::

Below the cell you just clicked run on, there should be an output saying Hello World.

Congratulations! You just programmed a computer to output text. Next step: ~~hacking the mainframe~~ learning about more Python fundamentals!
