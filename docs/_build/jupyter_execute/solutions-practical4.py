#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Practical 4 Solutions
The solutions for this practical are all written in jupyter notebook.


# ## Recursive Factorial

# In[55]:


def factorial(n):
    """
    Returns the Factorial of n
    :param n: an integer to calculate the factorial of
    :return: the factorial of n
    """
    if n == 1:
        return n
    else:
        return n*factorial(n-1)

# call function
print(factorial(4))


# ## Fibonacci Revisited
# The code below provides a solution for getting the *n*th element of the Fibonacci sequence.  To get the full sequence, the code below is not an efficient solution, and in this case the solution we did via iteration in Practical 2 is a better solution.

# In[51]:


import matplotlib.pyplot as plt
import numpy as np

def fibonacci(n):
    """
    Returns the Fibonacci sequence from 0 to the nth value in the sequence.
    :param n: positive integer
    :return: the nth Fibonacci value in the sequence
    """
    if n in {0,1}:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# In[52]:


# x and y coordinates
x = np.arange(1,20)
y = np.array([fibonacci(i) for i in x])

# plot n vs fibonacci(n)
fig, ax = plt.subplots()
ax.scatter(x,y)
ax.set(xlabel="n", ylabel="fibonacci(n)", title="The Fibonacci sequence")
# you do not need to call fig.show() in jupyter notebook to show your plot


# We can see from the plot above that the fibonacci sequence increases very fast.
# 

# # Tower of Hanoi
# 

# In[53]:


def tower_hanoi(n, source, target, spare):
    """
    Prints the sequence of steps required to solve the tower of Hanoi problem for n disck using 3 poles.
    :param n: number of disck
    :param source: name of source rod
    :param target: name of target rod
    :param spare: name of spare rod
    """
    if n == 1:
        print(f"Move disk 1 from {source} rod to {target} rod")
    else:
        tower_hanoi(n-1, source, spare, target)
        print(f"Move disk {n} from {source} rod to {target} rod")
        tower_hanoi(n-1, spare, target, source)


# In[54]:


# call the function for 3 disks with A as the source rod, B as the target rod and C as the spare rod.
tower_hanoi(3, "A", "B", "C")

