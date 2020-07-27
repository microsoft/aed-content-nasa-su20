# Exercise - Visualize the Machine Learning Model 

In this unit, we will use some of the libraries to visualize this prediction data.

```Python
# lets import a library for visualizing our decision tree
from sklearn.tree import export_graphviz

def tree_graph_to_png(tree, feature_names,class_names, png_file_to_save):
    tree_str = export_graphviz(tree, feature_names=feature_names, class_names=class_names,
                                     filled=True, out_file=None)
    graph = pydotplus.graph_from_dot_data(tree_str)  
    return Image(graph.create_png())
```

```Python
# this function takes a machine learning model and visualizes it
tree_graph_to_png(tree=tree_model, feature_names=X.columns.values,class_names=['yes','no'], png_file_to_save='decision_tree.png')
```