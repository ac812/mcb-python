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

# Creating functions

We have previously seen [what functions are and how to call them](calling-functions).  Functions are a good way to structure 
your code into useful chunks, each chunk being responsible for a particular task.  This makes functions a good way 
to create **reusable code**. In this section we are going to learn how to create a function of our own from scratch. 
Functions in Python are defined in the following way:

```{image} images/def-function.png
:align: center
```
where *parameters* is an optional list of zero or more comma separated parameters, and suite is one or more statements. The example code below defines a simple 
function which is named `hello`.  The function does not take any arguments, and it just prints *"Hello World!"* back.

```{code-cell} ipython3
def hello():
    print("Hello World!")
```
The definition of a function will not execute the code in it.  To execute the code in a function, you would need to call the 
function first:

```{code-cell} ipython3
hello()
```

The example below is another simple function, but this time, the function defines two parameters: `num1` and `num2`. The 
function below also returns the value of the sum of the two numbers (**arguments**) passed into the function by using the 
**`return`** keyword.  

```{code-cell} ipython3
def sum_two_numbers(num1, num2):
    return num1 + num2
```
Again, to execute the code inside the function we would need to call it.  The `sum_two_numbers()` function expects two arguments, below is 
an example.

```{code-cell} ipython3
print(sum_two_numbers(1, 1))
```

If you do not supply two arguments, the `sum_two_numbers()` would raise an error:

```{code-cell} ipython3
:tags: ["raises-exception"]
sum_two_numbers(1)
```

:::{card} Parameters vs Arguments
:class-card: sd-bg-light

{bdg-info}`Programming concept`

A **parameter** is the variable defined in the function definition inside the parentheses, for example, `num1` and `num2` are parameters
in the `sum_two_numbers()` function defined above.

An **argument** is the value that is passed into the function when it is called. In the call `sum_two_number(1, 1)` 1 and 1 are arguments.
:::

## Default argument values
You can assign default values to arguments in your functions, such that, if a user decides to call your function without 
specifying all the arguments, the arguments that were not passed would have already a predefined value.  For example, in the code 
below, `sum_two_numbers()` assigns default values of 0 to parameters `num1` and `num2`.  

```{code-cell} ipython3
def sum_two_numbers(num1=0, num2=0):
    return num1 + num2
```

Using the `sum_to_numbers()` function as defined in the code above, the `sum_two_number()` function can be called in 
different ways which are shown below:

```{code-cell} ipython3
print(sum_two_numbers())       #1
print(sum_two_numbers(0, 0))   #2
print(sum_two_numbers(0))      #3
```
The three function calls above return the same result, that of 0.  Line 1 makes use of both default values for `num1` and `num2`. 
Line 2 passes the values of 0 to `num1` and 0 to `num2` which happen to be the same as their default values.  Line 3 
calls `sum_two_numbers()` with only one argument.  The argument passed is assigned to the first parameter defined in the function, in this 
case this is `num1`.  `num2` will use its default value since no argument was passed for `num2`.  

## Positional vs keyword arguments

```{code-cell}
print(sum_two_numbers(1, 4))             #positional arguments
print(sum_two_numbers(num1=1, num2=4))   #keyword arguments
print(sum_two_numbers(num2=4, num1=1))   #not recommended
```
The function calls above also return the same result, this time it is 5.  However, the function calls above helps us understand 
better the difference between positional and keyword arguments.  **Positional arguments** are arguments that are passed without 
specifying the name of the parameter in the call.  The first line is an example of calling the `sum_two_numbers()` function 
with positional arguments.  **Keyword arguments** call functions using the name of the parameters in the form $parameter = value$. 
The second line is an example of calling the `sum_two_numbers()` function using keyword arguments.  The third call is also an 
example of the function call using keyword arguments.  However, it is not recommended to call functions in this way as essentially line 3 
is not following the same order the parameters were defined in the definition, which could lead to confusion.

The calls in the code below are all not recommended as they mix positional and keyword arguments in the same call. 
As a good practice, you should call functions using either positional arguments, or else using keyword arguments, but not both.

```{code-cell} ipython3
:tags: ["raises-exception"]

print(sum_two_numbers(1, num2=4))
print(sum_two_numbers(num1=1, 4))  #this raises an error
print(sum_two_numbers(1, num1=1))  #this raises an error
```

Line 2 raises an error as you cannot have a keyword argument followed by a positional one.  Line 3 also raises an error 
as both arguments are using the same argument; in the first argument, 1 is assigned to `num1` and the second argument is also assigning 1 to `num1`.

```{exercise} Exploring creating functions
:label: exploring-creating-functions

**Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`

Use the `sum_two_numbers()` function:  
a. What happens if you remove the `return` keyword from its definition?  
b. Explore default argument values, positional and keyword arguments by trying the code above and calling the `sum_two_numbers()` function with different arguments.

```

```{exercise} The Fibonacci sequence function
:label: fibonacci-function

**Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning`

Rewrite the solution of {numref}`fibonacci` such that, you create a function `fibonacci` that takes parameter `n` as an input, 
and returns the list of Fibonacci sequence numbers from 0 to `n`.

```




[//]: # (## Variable scope)




