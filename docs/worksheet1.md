---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
# Worksheet 1

```{exercise} Installing Python and PyCharm
:label: install
**Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`

Install Python and PyCharm on your personal computer if you have one.  Instruction on which versions you need and how 
to install these can be found [here](installation).
```


```{exercise} Running Python programs from the terminal
:label: running-terminal
**Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`

Take the code to run exercise {numref}`num-prog`. Save it into a file called *numbers.py* and run it from the terminal. Explain 
what you did to run the code in the terminal.
```

```{exercise} For loop
:label: for-words-exercise
**Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`

Take the code used to do {numref}`for-exercise` but this time, for each iteration, print the index of the word in list `l` next to the string.
```

```{exercise} Odd and even numbers
:label: odd-even
**Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`

Modify the code that identifies an [odd or even number](code-continue) to create a list of even numbers, 
and another list of odd numbers.  
```

````{exercise} Simple calculator
:label: calculator
**Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning`

Creat a program that works like a simple calculator:
* First, print a user menu that shows the operations available with this calculator:
 *1. Addition  
  2. Subtraction  
  3. Exit*  
* Then ask the user to enter two numbers.
* The calculutaor would then add or subtract these two numbers depending on the operation selected previously.  

```{tip}
The `input()` function is used to read in the user's input from the console.
```
````


````{exercise} Asterisk half-pyramid
:label: half-pyramid
**Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`

Draw a half pyramid as shown below using asterisks.  
\*   
\* \*   
\* \* \*   
\* \* \* \*   
\* \* \* \* \*  

```{tip}
Use **nested loops**: one loop inside another, with an outer loop to handle rows and an inner loop to handle columns.
```
````


`````{exercise} Asterisk full-pyramid
:label: full-pyramid
**Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning`

Draw a full pyramid using asterisks.

````{tip}
Use nested loops as in {numref}`half-pyramid` and think about the number of spaces and asterisk you need in each row as shown below:
```{image} images/full-pyramid.png
:align: center
```
````
`````

```{exercise} Debugging code
Debug the code above.  Put a breakpoint in the for loop and watch the values of the variables `spaces`, `i` and `j` change 
as you step over the code in each iteration.
```




