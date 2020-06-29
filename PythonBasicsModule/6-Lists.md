# Lists

Lists are ways that you can store a lot of data in Python (similar to variables). They are a collection of data types stored in the form of a list. Lists are very useful in Python because a lot of times you will need more than one piece of data. Also, lists are necessary for more advanced topics like machine learning.

## How to make a list

Defining lists in Python is very similar to creating variables. You must start by making a name for your list and then set it equal to a value. However, lists can hold multiple values. For example:

```python
# Create a list of common moon rocks
rockTypes = ["basalt", "highland", "breccia"]
rockTypes
```

>['basalt', 'highland', 'breccia']

As you can see, you must include square brackets and then include the data you want separated by commas.

Lists can have data that come in all forms (int, float, string, ext) and can even mix and match different types. For example:

```python
# A list with rock names and the number of that rock found
rockTypeAndCount = ["basalt", 1, "highland", 2.5, "breccia", 5]
rockTypeAndCount
```

>['basalt', 1, 'highland', 2.5, 'breccia', 5]

## List Functions

There are many pre-made functions, included in Python which we can use to modify a list.

For example, we can add items to a list by calling the .append() function followed by the data that we want to add in parenthesis. This will add an item to the end of a list. Let's add a rock type to our original list.

```python
rockTypes.append("soil")
rockTypes
```

>['basalt', 'highland', 'breccia', 'soil']

We can also delete items from the end of a list by calling the .pop() function. We will now delete soil from the rock types list.

```python
rockTypes.pop()
rockTypes
```

>['basalt', 'highland', 'breccia']

Finally, we can look and change an item from anywhere within the list. To see which item is at a certain point in the list, use square brackets after the list name to look at that specific item. Also, everything in Python is zero-based, meaning that counting begins at 0, not 1. So if we were to look at the first item in a list, we would use:  listName[0].  
In our rock type example, use the following code to look at the second item in the list:

```python
rockTypes[1]
```

>'highland'

We can also change a specific item in the list at a specific point by coding:
listName[item in list you want to change] = new data.  
In our rock type example, if we wanted to change the third item of the list to be "soil", we could do so by:

```python
rockTypes[2] = "soil"
rockTypes
```

>['basalt', 'highland', 'soil']

This will change the current value of the item at this spot of the list, so the previous data will be gone.
