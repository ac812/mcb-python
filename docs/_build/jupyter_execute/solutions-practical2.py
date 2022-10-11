#!/usr/bin/env python
# coding: utf-8

# # Practical 2 Solutions
# 
# ```{solution-start} exploring-creating-functions
# :label: exploring-creating-functions-solution
# :class: dropdown
# ```
# a.

# In[1]:


def sum_two_numbers(num1, num2):
    num1 + num2

print(sum_two_numbers(1, 1))


# In general, we should always aim to create functions that return a value, as a good programming practice.  However, in Python, a function that does not 
# specify a `return` statement, returns `None`by default.
# 
# ```{solution-end}
# ```
# 
# ```{solution-start} fibonacci-function
# :label: fibonacci-function-solution
# :class: dropdown
# ```

# In[2]:


def fibonacci(n):           #1      
    fib_seq = []            #2
    a, b = 0, 1             #3
    while a < n:            #4
        fib_seq.append(a)   #5
        a, b = b, a+b       #6
    return fib_seq          #7
                            #8
print(fibonacci(100))       #9


# Lines 1-7 define the `fibinacci()` function.  In line 2, `fib-seq` is an empty list that be populated in the `while` loop with 
# the Fibonacci sequence.  Instead of printing it, on line 5 we are adding the next item of the Fibonacci sequence to the 
# `fib_seq` list.  Line 7 returns the list.  Line 9 provides 100 as an argument to the `fibonacci()` function and then prints it.
# 
# ```{solution-end}
# ```
