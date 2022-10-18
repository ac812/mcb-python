#!/usr/bin/env python
# coding: utf-8

# # NumPy
# 
# ## What is NumPy?
# NumPy is a popular Python package for scientific computing.  It provides multidimensional arrays objects and functionality 
# for fast operations on them and facilitates mathematical operations.  NumPy is used in other popular Python packages including
# Pandas, SciPy, Matplotlib and scikit-learn.
# 
# ### NumPy arrays vs standard Python sequences (*e.g.,* lists)
# 
# Below are the main differences between NumPy arrays and standard Python sequences such as lists:
# * NumPy arrays can only contain the same type of data items, for example, you cannot have one data item as `int` and another as `str`.
# * Numpy arrays have a fixed size when they are created, and changing size of NumPy arrays will create a new array.  This is different to standard Python list which can grow dynamically.  
# * NumPy uses a **vectorised** code system for arrays, which enables the application of operations on each data item without the use of loops. This facilitates mathematical and other operations and has the following advantages:
#     * Fewer lines of code
#     * Fast (this is more evident with large list sizes)
#     * Easier to read, resembles mathematical notation.  The code below shows the code in standard Python code and in NumPy code that multiplies two lists:
# 
# `````{tab-set}
# ````{tab-item} Standard Python
# ```{code-block}
# for i in range(len(a)):
#     c.append(a[i]*b[i])
# ```
# ````
# 
# ````{tab-item} NumPy
# ```{code-block}
# c = a * b
# ```
# ````
# `````
# 
# ## Importing NumPy
# Because we are using the Anaconda distribution for Python, NumPy comes pre-installed.  You can check whether NumPy is installed 
# from the *Python Packages* tab in PyCharm.  
# ![python-packages](images/python-packages.png)
# 
# Once you have checked that it is installed on your machine, to be able to use NumPy we need to import it in the code.  The 
# widely adopted convention is as follows:

# In[1]:


import numpy as np


# ## Creating NumPy arrays
# A NumPy array is the main data structure of NumPy. We can create a NumPy array from a Python list as follows:

# In[2]:


a = np.array([55, 92, 110, 66, 75, 45, 40, 57, 55, 62])


# ```{figure} images/ndarray-pycharm.png
# ---
# name: ndarray-pycharm
# width: 60%
# ---
# `ndarray` object in PyCharm's Variable pane.
# ```
# 
# This creates an array object of type **`ndarray`** in memory as we can see from PyCharm's variable pane in {numref}`ndarray-pycharm`. 
# `ndarray` is short for "N-dimensional array", which means any number of dimensions. In NumPy: 
# * 1-D (one-dimensional) array is also called a **vector** and is similar to a Python list.
# * 2-D (two-dimensional) array is also called a **matrix**.
# * 3-D or higher dimensional arrays are also known as **tensor**.
# In this practical we will focus on vectors (1-D arrays) only.  
# 
# ```{figure} images/ndarray.png
# ---
# name: ndarray
# ---
# Representation of `ndarray` object in memory and its index positions of its data items.
# ```
# 
# {numref}`ndarray` above shows a representation of the `ndarray` object created in memory after running the code `a = np.array([55, 92, 110, 66, 75, 45, 40, 57, 55, 62])`. 
# In this example, variable `a` points to an `ndarray` object in memory.  As you can see, the `ndarray` object is composed of different attributes. 
# The data of the `ndarray` object is not stored inside the `ndarray` object, the `ndarray` object points to it.  We will be 
# looking at how we can use the `ndarray` object as we go along.  
# 
# NumPy arrays can be created using other functions.  The table below lists commonly used functions to create NumPy arrays.
# ```{list-table} Functions to create NumPy arrays
# :header-rows: 1
# :name: ndarray-create-table
# 
# * - Function
#   - Description
#   - Example
# * - `np.array(l)`
#   - returns a new `ndarray` object from list `l`.  </br> [Documentation to `np.array()`.](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy-array)
#   - `np.array([10, 20, 30])` returns `array([10, 20, 30])`.
# * - `np.zeros(shape)`
#   - returns a new `ndarray` object of length `shape` filled with zeros.</br> [Documentation to `np.zeros()`.](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html)
#   - `np.zeros(3)` returns `array([0., 0., 0.])`.
# * - `np.ones(shape)`
#   - returns a new `ndarray` object  of length `shape` filled with ones.</br>  [Documentation to `np.ones()`.](https://numpy.org/doc/stable/reference/generated/numpy.ones.html)
#   - `np.ones(3)` returns `array([1., 1., 1.])`.
# * - `np.arange(stop)` </br></br> `np.arange(start, stop)` </br></br>`np.arange(start, stop, step)`  
#   - `np.arange(stop)` returns a new `ndarray` object with a sequential range of data items from `0` to `stop`. </br></br> `np.arange(start, stop)` returns a sequential range of data items from `start` to `stop`. </br></br> `np.arange(start, stop, step)` returns a sequential range of `step`th data items from `start` to `stop`. </br></br>[Documentation to `np.arange()`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html).  
#   - `np.arange(3)` returns `array([0, 1, 2])`. </br></br> `np.arange(2, 5)` returns `array([2, 3, 4])`. </br></br> `np.arange(1,8,2)` returns `array([1, 3, 5, 7])`.
# * - `np.linspace(start, stop, num)`
#   -  returns a new `ndarray` with a `num` evenly spaced sequence of numbers from `start` to `stop`. </br> [Documentation to `np.linspace()`.](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)
#   - `np.linspace(-5, 5, 3)` returns `array([-5.,  0.,  5.])`. 
# ```
# 
# To get the length of an `ndarray` object use the `size` attribute as follows:

# In[3]:


a.size


# ```{exercise} Creating NumPy arrays
# :label: create-ndarrays
# 
# **Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`
# 
# 1. Try the examples in {numref}`ndarray-create-table` in the PyCharm console. For each example, look at the Variables 
# pane in the console to see the `ndarray` object created.  
# 2. Generate  a NumPy array that contains 20 evenly spaced numbers from 0 to 1.  What is the spacing between the numbers?  Hint: use [parameter `retstep`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html).  
# 3. Use the `np.full()` function to create a NumPy array with ten 0.1 values.
# 
# ```
# 
# 
# ## NumPy data types - `dtype`
# 
# NumPy is written in C, a low-level language.  Because of this, it inherits some features that are normally associated 
# with low level languages, NumPy data types are one of them.  
# 
# While the size of the standard Python data types (*e.g.,* `int`, `float`) offer flexibility, that is, 
# they can grow to accommodate numbers of different sizes (within the machine's memory constraints), NumPy data types 
# have fixed sizes. For example, in NumPy an `int` has several `dtype`s: `int8`, `int16`, `int32`, `int64`.  `int8` means 
# that a number created as `int8` will be stored in 8 bits or 1 byte of memory.  That is why the larger the number of bits 
# allocated to a number, the larger the range of numbers can be held. {numref}`integer-dtypes` below gives us an indication of the range 
# of numbers that can be held in the respective integer `dtype`.
# 
# ```{list-table} Number capacity for integer dtypes.
# :header-rows: 1
# :name: integer-dtypes
# 
# * - dtype
#   - Number capacity
# * - `int8`
#   - -128 to 127
# * - `int16`
#   - -32,768 to +32,767
# * - `int32`
#   - -2,147,483,648 to +2,147,483,647
# * - `int64`
#   - -9,223,372,036,854,775,808 to +9,223,372,036,854,775,807
# ```
# 
# Numpy also has `dtype`s equivalent to the corresponding standard Python data types:
# 
# ```{list-table}
# :header-rows: 1
# 
# * - Standard Python data type
#   - NumPy data type
# * - `int`
#   - `np.int_`
# * - `float`
#   - `np.float_`
# * - `str`
#   - `np.str_`
# * - `bool`
#   - `np.bool_`
# ```
# 
# When creating an array, NumPy automatically detects the type of data the array is made up of and allocates a data type that 
# fits that array based on several factors (including the computer's architecture).  Because of this, we do not need to worry about 
# which NumPy data type to allocate to our arrays as NumPy does that automatically for us.  In the case when we need to 
# specify the `dtype` argument in NumPy functions, in this course we will be using the standard Python data types.
# 
# 
# ```{exercise-start} dtype of NumPy arrays
# :label: dtype-ndarrays
# ```
# **Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`

# In[4]:


l = [55, 92, 110, 66, 75, 45, 40, 57, 55, 62]
a = np.array(l)


# 1. Using the code above: 
#    * What is the `dtype` of `a`? (Look into PyCharm's Variable pane to check the `dtype` of `a`).
# 2. What is the `dtype` of `np.zeros(3)`?  Why do you think this is the case?
# 3. Using list `l`, create a NumPy array that contains the values of `l` in `str` format.  What is the `dtype` of this array?
# 
# ```{exercise-end}
# ```
# 
# ## Array manipulation operations
# 
# ```{list-table} Array manipulation functions
# :header-rows: 1
# :name: ndarray-manip-table
# 
# * - Function
#   - Description
#   - Example
# * - `np.append(arr, values)`
#   - returns a new NumPy array with the `values` added to the end of array `arr`. Note: this does not change the size of `arr`, but a new `ndarray` object is returned with the appended values.
#   - `np.append(a, [1, 2, 3])` </br>`np.append(a, 1)`
# * - `np.insert(arr, index, values)`
#   - returns a new NumPy array with the `values` added at the `index` position of array `arr`.
#   - `np.insert(a, 3, 90)`  </br>`np.insert(a, 3, [1, 2, 3]`
# * - `np.delete(arr, index)`
#   - returns a new NumPy array with the data items in `index` deleted from `arr`. 
#   - `np.delete(a, 2)` </br>`np.delete(a, [2, 3])`
# * - `np.sort(arr)`
#   - returns a new NumPy array with the data items of `arr` sorted in ascending order.
#   - `np.sort(a)`
# * - `np.concatenate((arr1, arr2, ...))`
#   - returns a new NumPy array with the joined sequence of arrays.
#   - `a1 = [1, 2, 3]` </br> `a2 = [4, 5, 6, 7]` </br> `np.concatenate((a1, a2))`
# * - `np.unique(arr)`
#   - returns the unique data items in `arr`.
#   - `b = np.array([9, 3, 9, 8, 9, 4, 2, 0, 2, 5, 4, 7, 5, 1])` </br>`np.unique(b)`
# ```
# 
# ```{exercise-start} manipulating NumPy arrays
# :label: ndarrays-manip-exercise
# ```
# **Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`
# 
# 1. Try the examples in {numref}`ndarray-manip-table`.  Check the output of each example.
# 2. Sort NumPy array `a` in descending order
# 3. Create a NumPy array with the following values: [9, 3, 9, 8, 9, 4, 2, 0, 2, 5, 4, 7, 5, 1]
#    1. Get the frequency of each value in the array.
#    2. Get the index positions of the first occurring unique values in the array.
# ```{exercise-end}
# ```
# 
# ## Slicing NumPy arrays
# 
# We slice a NumPy array when we want to extract data items from it. Slicing in NumPy arrays works the same as slicing in 
# standard Python lists; using square brackets to specify the star, end and step of items we would like to extract from the NumPy array.  
# The code below provides a few examples:

# In[5]:


# extract data item at index position 2
a[2]
print(a[2])

# extract data items from index position 2 to index position 5 (excluded)
a[2:5]
print(a[2:5])

# extract every second data item from index position 1 to index position 2 
a[1:8:2]
print(a[1:8:2])


# ## Views and Copies of NumPy arrays
# 
# When we create a new variable (`b`) and assign it to an existing `ndarray` object (`a`), that variable will also point to the same `ndarray` object.
# {numref}`ndarray-assign` is a representation of this.
# 
# ```{figure} images/ndarray-assign.png
# ---
# name: ndarray-assign
# ---
# Representation of `ndarray` objects `a` and `b` in memory when `b = a`.
# ```
# 
# 
# Because of this, a change in `b` also effects `a`.

# In[6]:


# create a NumPy array a from list l
l = [55, 92, 110, 66, 75, 45, 40, 57, 55, 62]
a = np.array(l)

print("ID of a is:", id(a))

b = a
print("ID of b is:", id(b))

b[3] = 60
print(a)
print("ID of a is:", id(a))
print("ID of b is:", id(b))


# In the example above, `b` and `a` share the same object ID.  Changing the data item in index position 3 of `b`, caused 
# the change in `a` as well, since both are the same object.  
# 
# As we have seen in {numref}`ndarray`, NumPy arrays save their data separately from the `ndarray` object. The `view()` method of an `ndarray` object creates a new `ndarray` object that points to the same data of the base array. 
# Because it is pointing to the same data, any changes made to the view object will be effected in the base object which is 
# the `ndarray` where the array data is actually stored. In the example below `c` is the view object and `a` is the base object.
# As you can see the object ID of the base of `c` and `a` are the same.

# In[7]:


c = a.view()
print("ID of a is:", id(a))
print("ID of c is:", id(c))

c[3] = 62  #this changes also a
print(a)

print("ID of base array of c is:", id(c.base))


# ```{figure} images/ndarray-view.png
# ---
# name: ndarray-view
# ---
# Representation of NumPy view in memory.
# ```
# 
# Slicing a NumPy array also returns a view of it:

# In[8]:


d = a[2:5]
d[0] = 80    #this changes a[2] as well!
print(d)
print("ID of d is:", id(d))
print(a)
print("ID of a is:", id(a))


# When creating a **copy** of an `ndarray` however, this would create a completely new copy, that is, though the contents would
# be the same, the objects are two different ones in memory.  
# 
# ```{figure} images/ndarray-copy.png
# ---
# name: ndarray-view
# ---
# Representation of NumPy copy in memory.
# ```

# In[9]:


#create a copy of ndarray a
e = a.copy()
print("ID of a is:", id(a))
print("ID of e is:", id(e))

e[3] = 70
print(f"a is: {a}")
print(f"e is: {e}")


# ```{exercise-start}
# :label: ndarrays-view-copy-exercise
# ```
# **Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`
# 
# To understand the difference between views and copies of NumPy arrays, run the code in this section (Views and copies of NumPy arrays). 
# In each example, get the object ID of the NumPy array created and try to change a data item in the NumPy arrays. This should help 
# you understand whether the same object or same data is being processed in each case.
# ```{exercise-end}
# ```
# 
# 
# ## Vectorised array operations
# 
# One of the main differences between standard Python data sequences such as lists and NumPy arrays is that NumPy arrays use a vectorised system 
# which allows us to perform operations over all the `ndarray` object using one line of code as opposed to  using a loop as we do with lists.

# In[10]:


# Check whether each data item in a is > 60
a > 60

# If you try to the same with a standard Python list you would get an error
l > 60


# #Extract items in the list that are >60
# a > 60
# returns a list of True and False; True if the data item is > 60, and False otherwise.
# 
# <compare with standard python>
# 
# To get the actual data items we have to use our comparison statement inside the [] as essentially we want to slice our 
# ndarray based on a condition:
# a[a > 60]
# 
# This is similar to the way we extract items from vectors in R.  
# 
# You can combine multiple comparison statements using the & (and) and | (or) logical operators
# get the marks that are > 60 and < 90: 
# a[(a > 60)  & (a < 90)]
# 
# 
# ```{exercise-start} Odd and even numbers with NumPy arrays
# :label: odd-even-numpy-exercise
# ```
# **Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`
# 
# Using the list of integers: 55,  92, 110,  66,  75,  45,  40,  57,  55,  62  
# write code using NumPy arrays to print two list:
# 1. the even numbers from the list of numbers
# 2. the odd numbers from the list of numbers.
# ```{exercise-end}
# ```
# 
# ### Mathematical operations using NumPy arrays
# 
# Similarly, arithmetic operations can be performed on an array in one statement. For example:

# In[ ]:


a1 = np.array([10,20,30])
a2 = np.array([2,10,3])

# add arrays together
print(f"a1 + a2 is: {a1 + a2}")

#subtract
print(f"a1 - a2 is: {a1 - a2}")

#multiply
print(f"a1 * a2 is: {a1 * a2}")

#divide
print(f"a1 / a2 is: {a1 / a2}")


# You can also use aggregate functions on NumPy arrays that perform an operation across all items in the array and return one 
# result back.  For example, if you want to add all the numbers in a NumPy array together, use sum:

# In[ ]:


a3 = np.array([1, 4, 9])

#aggregation function
print(f"sum of all data items in a1 is: {a1.sum()}")
a1.min()
a1.max()
a1.mean()
a1.std() #get standard deviation


# In[ ]:


#return element-wise square root
ans = np.sqrt(a3)

# square each element in ndarray
# square(sqrt(x)) = x 
np.square(ans)

# calculate exponential of each data item
ans2 = np.exp(a2)

# calculate the natural logarithm of each data item in ndarray
# the natural logarithm is the inverse of the exponential function: log(exp(x)) = x
np.log(ans2)  


# There are several other mathematical functions that can be applied on ndarrays.  A full list can be found [here](https://numpy.org/doc/stable/reference/routines.math.html).
# 
# 
# 
# 
# ### Broadcasting
# 
# We have seen so far how we can perform arithmetic operations on NumPy arrays of the same size.  Broadcasting refers to when
# we want to perform an operation between a NumPy array of different sizes.  In this course we will be focusing on operations 
# between NumPy arrays and single values, for example, an integer.  In this case the integer is "broadcast" across the NumPy array
# so that they have similar sizes for the operation to be possible.

# In[ ]:


a1 * 2


# All these features make NumPy desirable to work with mathematical forumulas.  
# Eucleadean distance example:
# https://www.calculatorsoup.com/calculators/geometry-plane/distance-two-points.php

# In[ ]:


import numpy as np
 
# initializing points in
# numpy arrays
point1 = np.array((1, 2, 3))
point2 = np.array((1, 1, 1))
 
# finding sum of squares
sum_sq = np.sum(np.square(point1 - point2))
 
# Doing squareroot and
# printing Euclidean distance
print(np.sqrt(sum_sq))


# Exercise:
# https://numpy.org/devdocs/user/absolute_beginners.html#working-with-mathematical-formulas
# 
# 
# 
# 
# ### Random sampling
# To generate a random number we first call default_rng() method to create an instance of Generator

# In[ ]:


import numpy as np

seed = 12345
rng = np.random.default_rng(seed=seed)
#generate 3 random integers between 1 and 10 (excluded)
rints = rng.integers(low=1, high=10, size=3)
print(rints)

# generate 3 random decimal numbers in the range[0,1]
rfloat = rng.random(3)
print(rfloat)


# You can also draw samples from a distribution.  For example
# For a whole list of distributions see [here](https://numpy.org/devdocs/reference/random/generator.html#distributions)
# 
# #draw 5 samples from the normal distribution where mean=0 and standard deviation is 0.1
# mu, sigma = 0, 0.1 # mean and standard deviation
# sample_normal = rng.normal(mu, sigma, 5)
# print(sample_normal)
