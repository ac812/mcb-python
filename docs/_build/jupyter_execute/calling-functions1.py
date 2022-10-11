#!/usr/bin/env python
# coding: utf-8

# # Calling functions
# 
# :::{card} Functions
# :class-card: sd-bg-light
# 
# {bdg-info}`Programming concept`
# 
# Functions are a defined chunk of code which carries out a specific task or function. 
# :::
# 
# We have come across a few functions already *e.g.,* `print()`. Function names are always followed by parentheses and are 
# called in the following way *`function_name(argument1, argument2, ...)`*. They take an **input**, also known as an 
# **argument** (or arguments, if more than one) and after processing it **returns an output**.  One can think of a function 
# as a black box, where an input is fed in, the code inside the function will process it, and a processed output is returned. 
# This process is shown in {numref}`function` below.
# 
# ```{figure} images/function.png
# ---
# name: function
# ---
# A shows the different components of a function.  B shows an example of the function `abs()`.
# ```
# 
# In the example above, we see an example with the built-in function `abs()` which returns the absolute value of a number. 
# It takes as an input, -20, (the argument), and returns the processed output, 20.  A list of built-in functions in 
# Python can be found [here](https://docs.python.org/3/library/functions.html).  We will also be looking at how we can 
# create functions later on.  
# 
# 
# # Help
# The best place to find help in Python is using the [Python documentation](https://docs.python.org/3/) which contains 
# information about the Python syntax and about its functions and libraries.  It also contains a tutorial and other user 
# guides. The Python documentation is especially helpful when you are not familiar with a function, and so you would like to 
# understand how to use it. 
# 
# ```{figure} images/python-doc.png
# :width: 70%
# :name: python-doc
# 
# Searching the Python documentation for the `abs()` function.
# ```
# 
# In the example above in {numref}`python-doc`, we would like to understand how to use the function `abs()`.  We first search for the `abs` function 
# in the Python document *(panel A)*.  This returns a list of results.  The first item in the results returned is what we are looking 
# for as it says that `abs` is a built-in function *(panel B)*.  Upon clicking on that link we are redirected to the Python documentation
# about `abs()` *(panel C)* which provides more information about that function.  Note that in the documentation it is defined as 
# `abs(x)`.  `x` here is a **parameter**, which essentially means that it is a variable in the function definition.  This should be 
# distinguished from an argument which is the actual value passed to a function (in `abs(-20)` -20 is the argument).
# 
# Another way to get help on functions is via the `help()` function.  To access this form of help, type `help(abs)` in the 
# console.  This returns a shorter definition of `abs()` but most of the time this is enough.  Essentially you can pass 
# the function you want to know about as an argument to `help()`.
# 
# If none of these options was not enough to help you understand what you are looking for, there are several Python resources 
# on the internet that might have more information and provide examples.  A simple search sometimes would do the trick!
