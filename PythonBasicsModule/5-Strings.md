# Strings

Out of all the variables, strings are one of the most unique. This is because they can take on pretty much any key from your keyboard. Along with this, Python has a lot of pre-made code (functions) that you can call to manipulate your strings in various ways.

Lets start by making a string variable in Jupyter Notebooks. Copy the following line of code and click the run button:

```python
astronaut = "Dennis Ocampo"
```

Say we want to have this astronaut's name in all caps to print on his space suit. Instead of having to make a new variable, we can use the .upper() function to print his name capitalized. To call a function put the variable followed by a period, the name of the function and then parenthesis. Calling this upper function will not change the astronaut variable. You must set a new variable or current variable to that line.

```python
upperCase = astronaut.upper()
upperCase
```

>'DENNIS OCAMPO'

In a similar way, we can call astronaut.lower() to make the string lower case.

```python
lowerCase = astronaut.lower()
lowerCase
```

>'dennis ocampo'

Another cool string function we can use is called .capitalize(). This will make the first letter of a sentence capitalized and everything else lower cased. Try copying the new variable below and calling the capitalize functions.

```python
rocketOutput = "rOckEt iS A laUncH!"
rocketOutput.capitalize()
```

>'Rocket is a launch!'

Another neat thing you can do with strings in Python is concatenate or add them together. If you have two string variables you can add them together by simply using the + sign.

```python
launchLocationCity = "Cape Canaveral, "
launchLocationState = "Florida"

launchLocationCity + launchLocationState
```

>'Cape Canaveral, Florida'

Finally, you can use the * sign to repeat a string multiple times.

```python
artemisRoverSounds = "beep beep "
artemisRoverSounds * 3
```

>'beep beep beep beep beep beep '
