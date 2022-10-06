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

# Data Types
Data can be of many forms.  Python has several built-in data types.  The most commonly used data-types are below:

```{list-table} Common data-types in Python
:header-rows: 1
:name: data-types-table

* - Data Type
  - Description
  - Example
* - `int`
  - Integers (whole numbers)
  - 40
* - `float`
  - Numbers with decimal points (default)
  - 27.5
* - `Decimal`
  - Numbers with decimal points (high precision)
  - 27.5
* - `str`
  - Strings; sequence of characters
  - "Hello World!"
* - `bool`
  - Boolean; can only be `True` or `False`
  - 
```

## Float vs Decimal
When creating a variable and assign it a decimal number, that variable is automatically created of type 
`float` in Python.  This should be fine for most of the time but one issue is that some decimals are not represented 
precisely with float as seen in the example below.

```{code-cell} python3
import decimal

#use float to add 0.1 three times
x = 0.1 + 0.1 + 0.1

#check the value and data-type of x
print("Value of x is", x, "of type", type(x))
```
As shown in the example above the `float` version is inaccurate at the 17<sup>th</sup> decimal place.  These inaccuracies
however, are most of the time negligible. If you need high precision numbers, use `Decimal` numbers from the `decimal` 
module. `Decimal` numbers are slower to compute than `float` numbers, but they provide accurate results.  To make sure 
numbers are accurate provide the `decimal.Decimal()` function with the number value as a `string` as shown below:

```{code-cell} python3
import decimal

#use Decimal to add 0.1 three times
x = decimal.Decimal("0.1") + decimal.Decimal("0.1") + decimal.Decimal("0.1")

#check the value and data-type of x
print("Value of x is", x, "of type", type(x))
```

## Converting data-types (type casting)
We have already seen how to convert a `float` to a `Decimal` number.  To explicitly convert a variable from one type to another 
we use the following functions:

```{list-table} Common data-types in Python
:header-rows: 1
:name: casting-table

* - Function
  - Description
  - Example
* - `int(`x`)`
  - Returns an `int` version of number or string *x*.
  - `int("22")` returns `22`
* - `float(`x`)`
  - Returns a `float` version of number or string *x*.
  - `float(22)` returns `22.0`
* - `str(`x`)`
  - Returns a string version of *x*.
  - `str(22)` returns `"22"`
```
Every variable (object) in Python has a type.  The `type()` function returns the type of the object as in the example below:

```{code-cell} python3
a, b, c = 22, "22", 22.0

print(type(a))
print(type(b))
print(type(c))
```

```{tip}
The first line is an example of **multiple assignment** where instead of assigning values to a single variable one line at a time, 
you can assign values to multiple variables on the same line.  In the example above, `a` is assigned to `22`, `b` to `"22"` and `c` to `22.0`.  
```

## Watching variables
In PyCharm, checking the type of variables is much easier as PyCharm has a **Variables pane** where you can see all the variables of your existing program 
that are in memory, their type and also their values!  This is very convenient when you are writing code as you are always 
aware of what you have in memory.  The Variables pane can be found at the bottom of the screen on the right hand side in PyCharm in the Python 
Console tab as shown in the screenshot below.  This process is called **watching variables**.  
```{figure} images/variables-pane.png
---
name: variables-pane
---
Variables pane in PyCharm.    
It shows three variabels in memory (a,b,c), their types and their values.  
```

## Strings
Textual data is stored in `str` objects as shown in {numref}`data-types-table`.  We can distinguish a string object as it 
is enclosed in quotes `""`.

### String Escape Sequences
Strings can be enclosed in single quotes `‘ ‘` or double quotes `“ “`. In this course we will be using double quotes. 
Sometimes, you may want to include quotes as part of your string value.  This can still be done in Python by using Escape
sequences (see example below).  Special characters are escaped with backslashes `\` in strings.  The table below shows more Python String 
Escape sequences.

```{list-table} String Escape sequences.
:header-rows: 1
:name: data-types-table

* - Escape Sequence
  - Translation
* - \'
  - Single quote (')
* - \"
  - Double quote (")
* - \\
  - Backslash (\)
* - \t
  - Tab
* - \n
  - new line
```

Below is an example of a string that contains quotes:
```{code-cell} python3
a = "here is an example of 'single quotes' and \"double quotes\"."
print(a)
```

If you don’t want Python to interpret escaped characters, use `r` before the string as in the example below:
```{code-cell} python3
print(r"C:\home\textfile.txt")
```

### Formatted String Literals
Another useful operation with strings are formatted string literals, also known as **f-strings**.  F-strings allow you 
to include and format Python expressions in a string. They start with `f` or `F` followed by the string and accept 
expressions enclosed in `{ }`.  To understand better how f-strings work, below is an example using strings as 
expressions:

```{code-cell} python3
name = "Alexia"
location = "Cambridge"
print(f"My name is {name} and I live in {location}")
```
Now try one with your own name and location!  
f-strings are very useful when we need to format numbers.  To format decimal numbers up to a specified number of decimal 
places we use f-strings as following:

```{code-cell} python3
temperature = 27.78823

# display temperature to 1 decimal place
print(f"The temperature is {temperature:.1f}")
```
Here temperature is the `float` we want to print. After the `:` is the specification of how many decimal places we want it
to be printed `.1f`.



## Immutable objects
In Python, the built-in data types we have looked at so far, such as `str`, `int`, `float`, `Decimal`, `bool` are 
immutable.  This means, that once a value is assigned to them, that object cannot be changed. Every time we create a 
variable in Python and assign it a value, that value is created as an object in memory with a **unique object ID**.  If 
an object with the same value already exists in memory, however, Python will make your new variable point to this existing
object in memory.

To understand better how objects are created in memory the example below shows a step-by-step process of what happens
in memory when we create new variables and assign values to variables. 


```{figure} images/immutable-variables.png
---
name: immutable
---
Example of object references and objects.   
rc is the reference count (see [Garbage Collection](#garbage-collection) section).
```

If you want to check whether a variable is referencing the same object as another variable or not, use the `id()` function, 
which given a variable name as an argument, it returns the ID of an object in memory that the variable is pointing to. 
The code below further confirms the pointers shown in {numref}`immutable` by using the `id()` function.

```{code-cell} python3
# Step A
print("Step A")
a = 26
print("a is referencing object", id(a), "in memory")

# Step B
print("\nStep B")
b = a
print("a is referencing object", id(a), "in memory")
print("b is referencing object", id(b), "in memory")

# Step C
print("\nStep C")
a = "MCB"
print("a is referencing object", id(a), "in memory")
print("b is referencing object", id(b), "in memory")

# Step D
print("\nStep D")
b = a
print("a is referencing object", id(a), "in memory")
print("b is referencing object", id(b), "in memory")
```

## Garbage collection
All this memory management is done automatically for you in Python and you do not need to worry about allocating or 
freeing memory (as the case with some low level programming languages such as C).  Objects are garbage collected when they
have no object references pointing to them (such as the object with the value of 26 in the example above, at the end of the example code).  This 
process is known as **reference counting**.  When an object in memory has no variables pointing to it, it essentially 
means that the current program code does not need it anymore, so Python is free to garbage collect it.  For the garbage 
collection process to be triggered there is a threshold number of objects that need to be exceeded, that is, garbage
collection is not done immediately after an object has a reference count of 0.  

```{exercise} Variables and their types
:label: variables-types

**Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`

In this exercise we are going to explore the values and types of variables after performing oerations on them.  Watch the 
values of these variables in PyCharm as you proceed through the exercise.

Perform the following tasks:
1. Create two variables `a` and `b` and assign them the value of `10`.
2. Print the value and type of `a` and `b`.
3. Assign `a` to `22`.
4. What is the value of `a` and `b`?  What are their types?
5. Create a new variable `c` with the value of $a\div3$.
6. Print the value of `c` to 2 decimal places and its type.
7. Convert `c` to an integer and assign this result to variable `d`.
8. What is the value and type of `d`? Why do you think `d` has lost its fractional part from `c`?
```



