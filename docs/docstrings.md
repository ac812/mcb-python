## Documentation Strings
Now that we know how to create functions, it is important that we start creating them using good programming practice. We 
should follow the definition of a function with **docstrings**.  Docstrings is short for Python Documentation Strings.  docstrings
associate documentation with Python modules, functions and classes. To generate docstrings you need to use triple quotes as shown in the example below.

```{code-cell} ipython3
def sum_two_numbers(num1=0, num2=0):
    """
    Returns the sum of two numbers.
    :param num1: first number
    :param num2: second number
    :return: Returns the sum of num1 and num2.
    """
    return num1 + num2
```
PyCharm automatically generates the name of the parameters and the return statement.  Filling in the remaining details 
will ensure that we have documentation specified for the usage of our the function.  When we run code, similarly 
to comments, docstrings do not have an effect on our code.  But docstrings have the additional benefit of being associated with
documentation, so always use docstrings to explain functions rather than comments. 

To check out how the documentation created looks like, either include the `help()` function in your code using the name of the 
function you have created and documented with docstrings as an argument.  For example, `help(sum_two_numbers)`.  The other way 
is to call `pydoc` from the terminal together with the name of the file where the function is saved, for example, if `sum_two_numbers()`
was saved in `numbers.py`, then run `pydoc numbers.py` in the terminal.
