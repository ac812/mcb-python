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

# Worksheet 2


```{exercise} cm to m function
:label: cm-to-m
:class: dropdown
:nonumber:

**Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`

Create a function `cm_to_m()` that given a number `n` as an argument, which represents centimeters (cm), will convert that 
number to meters (m). 

```

```{exercise} Mark grading function
:label: mark-to-class
:class: dropdown
:nonumber:

**Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`

Write a program that returns the student class grade.  You may adapt [this code](code-reference-marking).
```


```{exercise} Even numbers function
:label: even-numbers-function
:class: dropdown
:nonumber:

**Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`

Write a function that given a list of numbers returns even numbers **only** back.
```

```{exercise-start} Bubble sort
:label: bubble-sort
:class: dropdown
:nonumber:

**Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning`
```

In this exercise we are going to practice **nested loops** by coding the bubble sort.  The bubble sort is a simple sorting 
algorithm. To sort a list of numbers, the bubble sort iterates over the numbers in the list.  For each number `l[j]`, 
it compares it with the number next to it `l[j+1]`.  If `l[j]` is bigger than `l[j+1]`, they will swap places, that is,
`l[j+1]` becomes `l[j]` and `l[j]` becomes `l[j+1]`.  This process is repeated for *N* times, where *N* is the length of the list - 1.

Below is an example of the first iteration of the bubble sort algorithm.  Write a `bubble_sort()` function that will implement 
the bubble sort algorithm as explained above.  The function should take a list of numbers as an input and returns 
the sorted list as an output. 

```{figure} images/bubble-sort.gif
:width: 50%
Example of the first iteration of the bubble sort algorithm.
```


```{admonition} Do you know?
:class: tip

The bubble sort is one of the simple sorting algorithms.  Because it is a simple algorithm it is not an efficient one and, 
in fact, it is widely critisised and also a known programmers humour.  [Barack Obama once joked about it too!](https://youtu.be/k4RRi_ntQc8)
```

```{exercise-end}
```
