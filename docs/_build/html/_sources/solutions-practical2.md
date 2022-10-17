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

# Practical 2 Solutions

```{solution-start} exploring-creating-functions
:label: exploring-creating-functions-solution
:class: dropdown
```
a.
```{code-cell} ipython3
def sum_two_numbers(num1, num2):
    num1 + num2

print(sum_two_numbers(1, 1))
```
In general, we should always aim to create functions that return a value, as a good programming practice.  However, in Python, a function that does not 
specify a `return` statement, returns `None`by default.

```{solution-end}
```

```{solution-start} fibonacci-function
:label: fibonacci-function-solution
:class: dropdown
```
```{code-cell} ipython3
def fibonacci(n):           #1      
    fib_seq = []            #2
    a, b = 0, 1             #3
    while a < n:            #4
        fib_seq.append(a)   #5
        a, b = b, a+b       #6
    return fib_seq          #7
                            #8
print(fibonacci(100))       #9
```
Lines 1-7 define the `fibinacci()` function.  In line 2, `fib-seq` is an empty list that be populated in the `while` loop with 
the Fibonacci sequence.  Instead of printing it, on line 5 we are adding the next item of the Fibonacci sequence to the 
`fib_seq` list.  Line 7 returns the list.  Line 9 provides 100 as an argument to the `fibonacci()` function and then prints it.

```{solution-end}
```

```{solution-start} create-ndarrays
:label: create-ndarrays-solution
:class: dropdown
```
b. 
```{code-cell} ipython3
import numpy as np

#retstep=True will also return the step size of the sequence generated
np.linspace(0, 1, 20, retstep=True)

a, step_size = np.linspace(0,1,20, retstep=True)
print(f"Step size of sequence is: {step_size}")
```
c. 
```{code-cell} ipython3
np.full(10, 0.1)
```
```{solution-end}
```

```{solution-start} dtype-ndarrays
:label: dtype-ndarrays-solution
:class: dropdown
```
1. `a` is of `dtype` `int64`.  NumPy detected that the values of the list supplied as argument are integers and so it created the `ndarray` with integer data types.
```{code-cell} ipython3
l = [55, 92, 110, 66, 75, 45, 40, 57, 55, 62]
a = np.array(l)
a.dtype
```
2., `b` is of `dtype` `float64`.  If we look at the documentation of [`np.zeros()`](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html), we notice that it has a keyword argument `dtype=float`.  This means that by default `np.zeros()` creates arrays of `dtype` `float64`.
```{code-cell} ipython3
b = np.zeros(3)
b.dtype
```
3.,  `c` is of type `<U3`.  Note that when creating strings NumPy does not use the `str` notation but instead uses a Unicode string. In this case, `U` means unicode and `3` is the length of the largest string in the array.  
```{code-cell} ipython3
c = np.array(l, dtype=str)
print(c)
c.dtype
```

```{solution-end}
```

```{solution-start} ndarrays-manip-exercise
:label: ndarrays-manip-exercise-solution
:class: dropdown
```
1. Note: NumPy array `a` is not changed, the methods return a new NumPy array object with the change requested.  
2.  The `np.flip()` function reverses the elements of a NumPy array.  
```{code-cell} ipython3
np.flip(np.sort(a))
```
3.1.
```{code-cell} ipython3
b = np.array([9, 3, 9, 8, 9, 4, 2, 0, 2, 5, 4, 7, 5, 1])

#get the frequency of each value in the array
unique, count = np.unique(b, return_counts=True) 
# unique values 
print(unique)
# frequency of these unique values 
print(count)
```
3.2.
```{code-cell} ipython3
#get the index position of the first occuring unique value
unique, indices = np.unique(b, return_index=True)
#unique values
print(unique)
# index positions of first occuring unique values 
print(indices)
```
```{solution-end}
```

