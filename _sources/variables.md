# Arithmetic Operations

Below are some of the most used mathematical operations.  

```{list-table} Numeric Operators and Functions
:header-rows: 1
:name: numeric-operators-table

* - Operator/Function
  - Description
  - Example
* - \+
  - Addition
  - 1 + 2 returns 3
* - \-
  - Subtraction
  - 3 - 1 returns 2
* - \*
  - Multiplication
  - 3 * 4 returns 12
* - /
  - Division
  - 4/2 returns 2.0
* - //
  - Floor division: returns the integer part of a division result (without the fraction part)
  - 5//3 returns 1
* - \%
  - Remainder
  - 5 % 2 returns 2
* - **
  - to the power of
  - 3 ** 2 returns 9
* - `pow(x, y)`
  - x to the power of y (same as **)
  - `pow(3, 2)` returns 9
* - `abs(x)`
  - absolute value of x
  - `abs(-5)` returns 5
* - `round(x, n)`
  - rounds x to n decimal places
  - `round(3.142, 2)` returns 3.14
```
Python follows the traditional mathematical rules of precedence (BODMAS).  You can find more about these rules 
[here](https://www.mathsisfun.com/operation-order-bodmas.html).

```{exercise} Arithmetic Operators
:label: arithmetic-operators

**Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`
  
a. Try the examples in {numref}`numeric-operators-table` in a jupyter notebook code cells.  
b. Calculate: $8 + (10 + 4^3 + 2)$
```


# Variables
The next sections of this practical are going to focus on the python code.  Try all the python code in these sections in the 
Jupyter Notebook **code cell** and run each cell to see the output.

If we want to write some useful code, we need to learn how to create variables.

:::{card} Variable
:class-card: sd-bg-light

{bdg-info}`Programming concept`

A variable (also known as **object reference**) is a reference name that points to a value in memory. A variable can be declared as following:  
**variable = value**
:::

Let us create our first variable:
```
weight_kg = 55
```
When executing this, Python creates an `int` object in memory with the value of `55` in it and creates a variable 
`weight_kg` that points to it.  Thus, in this example, the variable `weight_kg` has been assigned the value of `55` as 
shown in {numref}`variable`.

```{figure} images/varaiable.png
---
name: variable
---
Representation of a variable in memory.
```


When assigning a value to a variable, the Python interpreter does not print the value back.  To print the value of the 
variable you need to use the `print()` function (*e.g.,* `print(weight_kg)`).

## Variable naming conventions
Variables can be given any name, however it is important to follow the variable naming conventions in Python.  These conventions are in place as guidelines so that there is consistence in the way we write code.  A few rules to keep in mind when naming variables are:
* Variables are case-sensitive  (*e.g.,* `weight` and `Weight` are two different variables).
* Variables should be lowercase, with words separated by underscores *e.g.,* `weight_kg`
* Do not start variables with numbers.
* Use only letters (underscores and digits if necessary).
* Variables should be descriptive to improve readability *e.g.,* `asdjks` is not a good variable name.
* Variables should not be too long *e.g.,* `this_is_my_weight_in_kg` is not a good variable name.
* Do not use function names, class names, data types or other [keywords]( https://docs.python.org/3/reference/lexical_analysis.html#keywords) as variable names.

Detailed guidelines on Python naming conventions can be found in the [PEP 8]( https://peps.python.org/pep-0008/#function-and-variable-names); the de facto code style guide for Python and [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html#316-naming).
