# Variables

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
