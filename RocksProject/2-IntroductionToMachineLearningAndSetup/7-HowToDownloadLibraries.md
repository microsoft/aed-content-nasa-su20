# Downloading AI Libraries

It may seem like there are a lot of libraries that we must download for this project. Luckily, there is a software called Anaconda that lets us download all of the libraries very quickly. Microsoft has a [video about downloading and configuring a similar environment](https://www.youtube.com/watch?v=5E3WMb8_T3s&list=PLlrxD0HtieHjDop2DtiCmwTTcrlwKAVHE&index=8) to the one we need, but continue reading to download the right libraries for this project.

## Download Anaconda

Start by going to the [Anaconda Download page](https://www.anaconda.com/products/individual) to begin installing Anaconda. Click on the download button and walk through the steps to install it to your computer.

## Create an environment with AI libraries

Now that we have Anaconda installed, bring up the anaconda prompt. You can do this by searing for "anaconda" on your computer. Once you have the anaconda prompt open type the following:
`conda create -n myenv python=3.7 pandas jupyter seaborn scikit-learn keras pytorch pillow`

This code will begin installing all of the libraries we need through Anaconda. Note, we are having you download a few other libraries, but these are good data science libraries that may be useful in the future.
You will be prompted to install the packages, type 'y' and then enter.

Finally, you will have to activate your new environment. To do this type:
`conda activate myenv`

This new environment should be created and ready to use. There is one more library that we need to add to the environment that cannot be downloaded in this way.

## Install torchvision to environment

To install torchvision, in the anaconda prompt type:
`conda install -c pytorch torchvision`

You will once again be asked to type 'y' and then enter.

You now have an environment built that will be able to take you through the rest of the program. Make a new Jupyter notebook file and set your environment to be this new one you just created.
