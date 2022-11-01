#!/usr/bin/env python
# coding: utf-8

# # Recursive functions
# 
# We have previously looked at **iteration** (`for` and `while` loops) as the mechanism to repeat a set of statements in our code. We will 
# now be looking at **recursion** which is another way for repeating a set of statements.  A **recursive function** is a function 
# that calls itself. The code below shows an example of a recursive function `sum_to_n()` which adds the numbers from 1 to 
# `n`. For example, when `n` is 4, `sum_to_n(4)` will give the following answer: 1+2+3+4 = 10.
# 
# ```{code-block}
# def sum_to_n(n):                   #1
#     if n == 1:                     #2
#         return 1                   #3
#     else:                          #4
#         return n + sum_to_n(n-1)   #5
# ```
# 
# A recursive function has the following properties:
# 1. has a based case 
# 2. has a general case, that moves towards its base case
# 
# If a recursive function does not have these properties, then it will continue calling itself until it uses all memory available 
# to it, which is also known as **stack overflow**. The **general case** is a statement that expresses the same problem but in a smaller version of it.  In the code above line 5 is the general case. 
# Here the function is calling itself using the argument `n-1` (smaller version). The **base case** is the statement that terminates recursion, or stopping condition. 
# When `n` is 1, `sum_to_n()` returns 1.  When the base case is reached, the process starts to **unwind**, because since we know
# the answer of `sum_to_n(1)`, we are now able to compute the answer of the other recursive calls.  
# 
# Whenever a function is called, an entry is made to the function's **call stack**, known as a **stack frame**. The stack frame contains
# information about the value of the local variables of the function and the position in the function that was last reached before calling another 
# function.  In this way, the call stack keeps track of the execution of a program. The animation below shows an example of this process
# using the example code above.
# 
# ```{figure} images/recursion.gif
# ---
# name: recursion-anim
# ---
# Tracing the execution of the `sum_to_n()` recursive function
# ```
# 
# In Step 1, the function starts running until it reaches line 5 where it calls itself. A stack frame for the first function 
# call is **pushed** to the call stack. This process is repeated until Step 4. In Step 4, the base case is called and `sum_to_n(1)` is 
# evaluated to 1 and the function terminates.  Because we have an actual value, that stack frame is **popped** and the call stack pointer now moves to the previous stack 
# frame. Control now returns to line 5 at the state in specified in stack frame in Step 5. This can now evalautes to 3 and the return statement in line 5 causes the 
# function to terminate, which then pops the stack frame and moves the pointer to the previous one. This process continues until the call stack is 
# empty which would mean that all the recursive calls have been evaluated and the code in `sum_to_n()` has been executed. An in fact, in step 8, we now have the sum of all numbers up to n which 
# is 10 in this case.  
#  
# 
# 
# ```{exercise-start} Fibonacci revisited
# :label: fibonacci-revisited
# ```
# **Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning`
# 
# Write a recursive function to generate the first 20 (*n*) Fibonacci sequence.  Plot  *n* against *fibonacci(n)* as a scatter plot.
# Notice the pattern of the points on the plot.
# 
# ```{exercise-end}
# ```
# 
# 
# [//]: # (```{exercise-start} Factorial)
# 
# [//]: # ()
# [//]: # (```)
# 
# [//]: # (**Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning`)
# 
# [//]: # ()
# [//]: # (```{exercise-end})
# 
# [//]: # (```)
# 
# ```{exercise-start} The Tower of Hanoi
# :label: tower-hanoi
# ```
# **Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning`
# 
# In this exercise we are going to solve a classic mathematical puzzle:  **The Tower of Hanoi**.
# This puzzle is associated with a legend of a Hindu temple where the puzzle was used to increase the mental discipline of priests [^1].
# 
# The puzzle consists of 3 rods and *n* disks placed in order of decreasing size (small disk at the top, large disk at the bottom).
# In this example we are going to use 3 disks. 
# <insert image here>
# 
# The puzzle is solved when the disks are moved from rod A to rod B, following the rules below:
# 1. Only one disk can be moved in each step
# 2. Each step consists of moving the upper disk into a new rod
# 3. No disk can be placed on a smaller disk
# 
# The animation below shows the steps involved to solve the Tower of Hanoi puzzle using 3 disks.
# ```{figure} images/hanoi.gif
# ---
# name: tower-hanoi-img
# ---
# The sequence of steps to solve the Tower of Hanoi problem.
# ```
# The minimum number of steps required to solve the Tower of Hanoi puzzle is $2^n - 1$, where *n* is the number of disks.
# 
# The best way to solve this puzzle is by observing the pattern that is used to solve it.  Below is the algorithm:
# 
# ```{prf:algorithm} Tower of Hanoi
# :label: hanoi-algorithm
# 
# if disk == 1  
#  &nbsp;&nbsp;&nbsp;   move disk from source rod to destination rod  
# else  
# &nbsp;&nbsp;&nbsp;    recursively move disks 1 to $n-1$ from source rod to the spare rod  
# &nbsp;&nbsp;&nbsp;    move disk $n$ from source rod to the target rod  
# &nbsp;&nbsp;&nbsp;    recursively move 1 to $n-1$ from spare rod to the target rod  
# ```
# Write a recursive function to solve the Tower of Hanoi puzzle.  For each step write the move each disk is doing, for example:  
# "Move disk 1 from A rod to B rod"  
# Call the function using 3 disks.
# 
# ```{exercise-end}
# ```
# 
# [^1]: https://en.wikipedia.org/wiki/Tower_of_Hanoi
