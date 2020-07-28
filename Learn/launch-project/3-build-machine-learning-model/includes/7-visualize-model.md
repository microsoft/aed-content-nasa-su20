# Exercise - Visualize the Machine Learning Model 

One of the benefits of using a decision tree classifier is the visualization that you can use to better understand how the model makes decisions. Using `graphviz` and `pydotplus` you can quickly see how a decision is made and in future iterations, you can see how the decisions are changed.

## Create the Visual Tree

To create a visual representation of the model, you will create a simple function that takes in as parameters:
- Data: `tree` - this is the machine learnign model
- Columns: `feature_names` - this is a list of the columns in the input data
- Output: `class_names` - this is a list of the options for classification (in this case, yes or no)
- File Name: `png_file_to_save` - this is the name of the file where you want to save the visualization

You will call [scikit-learn's `export_graphviz()` function](https://scikit-learn.org/stable/modules/generated/sklearn.tree.export_graphviz.html) and then return an image representation of the graph that scikit-learn gives you:

```Python
# lets import a library for visualizing our decision tree
from sklearn.tree import export_graphviz

def tree_graph_to_png(tree, feature_names,class_names, png_file_to_save):
    tree_str = export_graphviz(tree, feature_names=feature_names, class_names=class_names,
                                     filled=True, out_file=None)
    graph = pydotplus.graph_from_dot_data(tree_str)  
    return Image(graph.create_png())
```

Calling this function if fairly straightforward:
- Data: `tree_model` - The model you trained and tested earlier
- Columns: `X.columns.values` - The list of columns in the input
- Output: [`yes`,`no`] - The two possible outcomes
- File Name: `decision_tree.png` - The name of the file where you want to save the image

```Python
# this function takes a machine learning model and visualizes it
tree_graph_to_png(tree=tree_model, feature_names=X.columns.values,class_names=['yes','no'], png_file_to_save='decision_tree.png')
```

This will create this image:  
![Visualization of decision tree](Learn\launch-project\3-build-machine-learning-model\media\decision_tree.jpg)

## Understanding the Visualization

This simple tree shows you that the most important feature of the data was the Wind Speed at Launch Time. If the wind speed was less than 1 then 192 of the 240 samples were correctly guessed to be a launch. 191 of those samples only needed the `Wind Speed at Launch Time` to be above 1 in order to correctly guess the outcome, while 1 required more information.

This isn't very good insight, however, since in LP3M2U5 we set all values to 0 that were empty, and we know that a lot of the values that were related to the *time of launch* were 0 since 60% of our data was not related to an actual launch or attempted launch.

Continuing to look at the tree you can see that `Max Wind Speed` is the next most important feature of the data. Here you can see that of the remaining 49 days when the max wind speed was greater than 30.5, 48 of them yielded a correct "no launch" output and one of them yielded a "yes launch" output. 

This might be more interesting because there was only one day where a launch was planned and the `Max Wind Speed` was greater than 30.5, which was May 27, 2020 - the Space X Dragon launch that was then post-poned to May 30, 2020. 

## Improving the Results

With this visualization you were able to see that some features became really important, but it was based on incorrect information. 

One improvement that could be made is to determine the relationship between `Max Wind Speed` and `Wind Speed at Launch Time` for the rows that have that information. Then, instead of making `Wind Speed at Launch Time` 0 for non-launch days, it could have been made to be the estimate of what it would be at a common launch time. This might have represented the data better. 

Can you think of other ways to improve the data?