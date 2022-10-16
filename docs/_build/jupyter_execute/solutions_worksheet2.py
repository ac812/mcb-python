#!/usr/bin/env python
# coding: utf-8

# # Worksheet 2 Solutions
# 
# ```{solution-start} cm-to-m
# :label: cm-to-m-solution
# :class: dropdown
# ```

# In[1]:


def cm_to_m(n):
    """
    Returns the meter conversion of a number.
    :param n: integer containing the centimeter value to be converted.
    :return: Returns the meter conversion of the integer argument n.
    """
    return n/100

print(cm_to_m(345))


# ```{solution-end}
# ```
# 
# 
# ```{solution-start} mark-to-class
# :label: mark-to-class-soliution
# :class: dropdown
# ```

# In[2]:


def get_grading(mark):
    """
    Returns the class that the mark passed as an argument falls under.
    :param mark: integer containing the student mark which ranges from 0 - 100.
    :return: The class that the mark falls under.
    """
    if mark > 69:
        return "First"
    elif mark > 49:
        return "Second"
    elif mark > 39:
        return "Third"
    else:
        return "Fail"

print(f"77 is in class: {get_grading(77)}")
print(f"55 is in class: {get_grading(55)}")


# ```{solution-end}
# ```
# 
# 
# ```{solution-start} even-numbers-function
# :label: even-numbers-function-soliution
# :class: dropdown
# ```

# In[3]:


def is_even_num(l):
    """
    Retrurns the even numbers from a list of arguments passed as an argument to this function.
    :param l: list of numbers.
    :return: Even numbers from the list l passed as an argument to this function.
    """
    enum = []
    for n in l:
        if n % 2 == 0:
            enum.append(n)
    return enum

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(is_even_num(l))


# ```{solution-end}
# ```
# 
# 
# ```{solution-start} bubble-sort
# :label: bubble-sort-solution
# :class: dropdown
# ```

# In[4]:


def bubble_sort(x):
    """
    Returns the list of integers x in ascending order.
    :param x: list of integers
    :return: the sorted list of integers in ascending order
    """
    k = len(x)
    for i in range(k-1):
        for j in range(k-i-1):
            if(l[j] > l[j+1]):
                l[j], l[j+1] = l[j+1], l[j]
    return l


l = [3, 1, 6, 2, 4]
print(f"Initial list: {l}")
print(f"Sorted list: {bubble_sort(l)}")


# Note:  there are different versions of optimisations of the bubble sort that I have not included in this solution as it is 
# outside the scope of this exercise.  However, if interested please look into *bubble sort algorithm optimisations*.
# ```{solution-end}
# ```
