# The Human Classifying Process

Before we build an AI system to detect the rock types, lets see how we 'humans' do it.

This is the likely process that our brain goes through to do this:

### Step 0

We have to collect as many rock images as possible

Fortunately Microsoft has a great relationship with Nasa and has provided us 1000's of rock images

### Step 1

Our brain first tries to extract patterns from each image, patterns such as:

Color combinations
Sharp edges
Circular patterns
Texture of the rock
Size of the rock

Our brains subconsciously do all of these without us noticing. We call these 'Features' in AI.

<img src="../Media/features.png" width="350" align="center">  

### Step 2

Next, we try to find the relationships between the features and rock types

In this step our brain tries to figure out what are the characteristics/features of each rock type
As a result of this, we will come up with some rules, for example : "Darker rocks are usually Crustals". "Basalt rocks have more dense textures", ...
We show these associations with links such as shown below:

<img src="Media/links.png" width="350" align="center">

### Step 3

Given a new rock image, our brain extracts all of its characteristics we discussed above, and then uses the associations we made in the second step to decides what type of rock it is.

<img src="Media/dl.png" width="550" align="center">