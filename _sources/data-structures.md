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

# Data Structures
So far we have dealt with single data items.  But what if we have a large number of data items? Storing each item in a 
separate variable is not efficient and time-consuming.  This is when we use data structures.

:::{card} Data Structures
:class-card: sd-bg-light

{bdg-info}`Programming concept`

Data structures are structures in memory that store and organise data. Essentially it is a collection of data items.
:::
 
The benefits of having multiple data items in a collection makes it easier to perform operations that need to be applied 
on each item in the collection.  Data Structures are also very useful when reading data from files.  This section introduces
different data structures commonly used in Python.  

##  Tuples
Tuples are one of the built-in data structures in Python.  Tuples can contain data items of different data types, but as 
a good practice we normally create lists of the same data tyoe.  Tuples are created as a comma-separated list of data items enclosed 
in parentheses.  Let us create our first tuple:

```{code-cell} python3
t = (55, 92, 110, 66, 75, 45, 40, 57, 55, 62)
```
The code above creates a variable `t` which references a tuple in memory that is 10 items long.  Assigning data items to
a tuple is also known as **tuple packing**.  

### Tuple index positions and slicing

Each data item has a specified position known as **index position**.  Index positions in Python start from **0**. {numref}`tuple` below shows an
example of the sequence of data items in tuple `t` together with their index positions.

```{figure} images/tuple.png
---
name: tuple
---
Representation of tuple `t` in memory and the index positions of its items.
```

A tuple is a **Sequence type** in Python, and therefore, it can be sliced using the item access operator `[]`.  **Slicing** 
means extracting items from a sequence.  Assuming `seq` is a sequence, in this case of data items, to extract one item from a tuple, specify the index position of that item in  `[]` 
as $seq[index position]$ as in the example below.

(code-tuple-indexing)=
```{code-cell} python3
#Extract item at index position 2
print("Item at t[2] is", t[2])


#Extract item at index position -2
print("Item at t[-2] is", t[-2])
```

To extract more than one item from a sequence you can either:
* $seq[start:end]$ to extract items from a sequence from a *start* position up to an *end* position (excluding it).
* $seq[start:end:step]$ to extract every *step<sup>th</sup>* item from the sequence starting from the *start* 
position to the *end* position (excluding it).
Below are two examples, A and B, that show these two ways of slicing a tuple.

```{figure} images/tuple-slicing.png
---
name: tuple-slicing
---
Tuple slicing.
```

(code-reference-tuple-slicing)=
Below are code examples of other operations you can do with tuples:
```{code-cell} python3
#Extract items from the beginning of the tuple to index position 2 (excluded).
print("t[:2] is", t[:2])

#Extract items from index position 5 to the end of the tuple.
print("t[5:] is", t[5:])

#print all items in a tuple
print("\nPrint all items in tuple t", t)

# Tuple concatenation: add tuples together
t2 = t + (70,)   #you have to specify the one item as a tuple as well
print("\nConcatenate t to (70,) results in", t2) 

# Tuple replication:  replicate contents of a tuple by a specified number of times
t3 = t * 2
print("\nReplicating tuple t by 2:", t3)

# Tuple unpacking - place data items of tuple in separate variables
print("\nTuple unpacking:")
t4 = ("Alexia", "MCB", "1B")
(name, subject, year) = t4
print("Name is", name)
print("Subject is", subject)
print("Year is", year)
```

### Tuples are immutable
As mentioned previously, tuples are immutable, meaning that they cannot be changed. Below is an example showing what will happen 
if we try to change the contents of a tuple. 

```{code-cell} ipython3
:tags: ["raises-exception"]
# change the data item at index position 2 of tuple t
t[2] = 80
```

As you can see an error is thrown back saying explicitly that the `'tuple' object does not support item assignment`. Since they
cannot be modified, tuples are useful when you have a fixed sequence of data items that you know are not going to be changed, 
*e.g.,* days of the week, months of the year. Another benefit of tuples is that they are 
faster than [lists](#lists).  However, this depends on the size of your data and the difference is normally not significant.

If you want to be able to modify the sequence of data items, then [use a `list` instead](#lists).  You can convert
a tuple to a list by the `list()` function *e.g.,* `l = list(t)` will create a variable `l` of type `list` that contains the 
same data items as `t`.  


### Membership operators
Membership operator are used to test for membership in Sequence types.  For tuples, the `in` **membership operator** 
returns `True` if a data item in tuple `t` is equal to `x`, otherwise it returns `False`. The `not in` **non-membership operator** 
does the opposite, it returns `True` if a data item in tuple `t` is not equal to `x`, otherwise it returns `False`.  The code
below shows an example of using membership operators in tuples.

(code-reference-tuple-membership)=  
```{code-cell} ipython3
:tags: ["remove-output"]
#Check if number 2 is one of the items of tuple t
2 in t      #returns False

#Check if number 55 is one of the items of tuple t
55 in t     #returns True

#Check that 2 is not one of the items of tuple t
2 not in t  #returns True
```

### Other useful functions

Below is a list of other useful functions that can be used with tuples.  Note that these functions do not make any changes 
on the tuples, but rather they perform a calculation or operation on the data items of the tuple and return the result.

```{list-table} Useful functions for operations with tuples
:header-rows: 1
:name: tuple-utility-functions

* - Function
  - Description
  - Example
* - `len(t)`
  - returns the number of data items in a tuple `t`.
  - `len(t)` returns 10
* - `min(t)`
  - returns the smallest data item in `t`.
  - `min(t)` returns 40
* - `max(t)` 
  - returns the largest data item in `t`.
  - `max(t)` returns 110 
* - `t.index(x)`
  - returns the index of the leftmost index position of data item `x` in tuple `t` or throws an error if `x` is not present.
  - `t.index(55)` returns 0
* - `t.count(x)`
  - returns the number of times `x` is present in `t`.
  - `t.count(55)` returns 2
``` 



## Lists
Lists hold a one dimensional list of data items.  This is similar to tuples, however they differ from tuples over two main things:
1. how they are declared
2. they are mutable objects

Lists are declared as a comma-separated list of data items enclosed in square brackets, rather than parentheses.  Let us 
create a list `l` with the same data items as tuple `t` above:

(code-reference-list)=
```{code-cell} python3
l = [55, 92, 110, 66, 75, 45, 40, 57, 55, 62]
```

Lists are also a Sequence type in Python and therefore support slicing, membership operators, concatenation, replication 
and the other utility functions we mentioned in the [Tuples](#tuples) section.

```{exercise} Exploring lists
:label: exploring-lists

**Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`

Explore lists by trying the code we used in the [Tuples](#tuples) section as follows:
1. Create a list using the [code above](code-reference-list).
2. Explore list index positions by adapting [this code](code-tuple-indexing).
3. Explore list slicing by adapting the code in {numref}`tuple-slicing` and [this code](code-reference-tuple-slicing).
4. Test for membership of data items in lists using the membership operators as in [this example](code-reference-tuple-membership).
5. Try other useful functions on lists as specified in {numref}`tuple-utility-functions`.
```

### Lists are mutable
Unlike tuples, lists are mutable, this means that we can modify lists.  Example:

```{code-cell} python3
#print contents of l and get id of l
print(l)
print("l is referencing object", id(l), "in memory")

# change the data item at index position 2 of list l
l[2] = 80
print("\nAfter l[2] = 80, l is:", l)
print("l is referencing object", id(l), "in memory")
```
When we tried to apply a [similar operation in tuples](#tuples-are-immutable), Python threw an exception, because tuples are immutable.  Since 
lists are mutable, the code above changes the data item in index position 2 successfully in `l`.  


### List utility methods

In addition to the sequence methods in {numref}`tuple-utility-functions`, we can use other methods with lists.  
This is mainly because lists can be modified.

```{list-table} List utility methods
:header-rows: 1
:name: list-utility-methods

* - Function
  - Description
  - Example
* - `l.append(x)`
  - appends data item `x` at the end of list `l`.
  - `l.append(100)`
* - `l.insert(i, x)`
  - insert data item `x` in list `l` at index position `i`.
  - `l.insert(1,44)`
* - `l.remove(x)`
  - removes the leftmost occurance of the data item that is equal to `x` or throws an error if `x` is not present in list `l`.
  - `l.remove(55)`
* - `l.reverse()`
  - reverses the data items in `l`
  - 
* - `l.sort()`
  - sorts the data items of list `l` in ascending order.
  - 
* - `del l[start:end]`
  - The `del` statement removes the data items from start position to end position (excluded) in list `l`.
  - `del l[7:9]`
```

```{admonition} Methods vs Functions
:class: tip

We have already seen how to call functions.  Functions are called only by their names, eg. `print()`. Methods are similar 
to functions but they are  defined inside classes or objects, and so they are dependent on them. We will not be going 
into the details of object-oriented programming in this course, but we have already encountered some methods in tuples and 
lists that use methods *e.g.,* `l.append(`x`)`.  Here `l` is an object reference of the `list` class and `append()` is a method 
inside the `list` class.  The dot `.` after `l` is used to access the method associated with the `list` object. In this example, 
a pop-up menu will be shown in PyCharm with the list of all methods associated with `list`. 

```

```{exercise} 
:label: lists-utility

**Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`
  
Try the examples in {numref}`list-utility-methods`. Check the output of list `l` after running every example.
```


