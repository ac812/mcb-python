# Practical 3
# Data visualisation and Manipulation

## Aim  
In this practical we will build further our Python skills.  So far we have worked on one-dimensional datasets.  In this practical 
we will learn how to work with tabular (two-dimensional) datasets using the Pandas package.

## Objectives
During this practical you will learn how to:
* create a 2D NumPy array (matrix)
* handle matrices
* load tabular data in Python using the Pandas package
* manipulate tabular data
* visualise tabular data
* code the Collector's coupon problem


## Instructions

The best way to do this practical is to read the associated notes which will introduce you to the core concepts of Python programming. 
These notes are designed with all the details you would need to be able to perform the exercises in this practical. In 
general, you would not need to refer to additional texts and resources as these notes have been explained in detail with
accompanying visual aids and examples to explain concepts to beginners.  Apart from the exercises listed below, there are also 
examples throughout the notes which provide insight on the concepts introduced, and therefore, it is recommended that you also 
run these examples as you progress through the practical notes.  

**If you are an experienced Python programmer**, you might find that you already know about the content in these notes. You 
may want to skip sections of notes that you already know and attempt the exercises that are at the higher levels. 

### Exercises levels
Exercises in this practical are labelled with the level of difficulty of the respective exercise:

```{list-table}
:header-rows: 1

* - Level
  - Description
* - {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`
  - **Level 1**:  Excercises in Level 1 are simple excersises designed to get you familiar with the Python syntax.  If you already know how to program in Python, you may skip these exercises.
* - {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`
  - **Level 2**: Excercises in Level 2 combine different Python programming concepts to solve simple problems.  
* - {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning`
  - **Level 3**: Exercises in Level 3 test not just the understanding of the Python syntax but also how Python can be used to solve problems.  
```

### Exercises

This practical is composed of the following exercises:

```{list-table}
:header-rows: 1

* - Exercise
  - Description
  - Level
* - {numref}`matrix-manip-exercise`
  - **Manipulating NumPy Matrices**:  This exercises performs different NumPy matrix manipulations.
  - {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`
* - {numref}`shaping-matrix`
  - **Shaping a matrix**:  In this exercise we will learn how to shape a matrix to the desired shape.
  - {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`
* - {numref}`sum-columns-matrix`
  - **Calculate sum of columns of a matrix**:  In this exercise we will learn how to calculate the sum of the columns of a matrix.
  - {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`
* - {numref}`exploring-df`
  - **Exploring the DataFrame**:  In this exercise, we first load data from a .csv file and then explore the DataFrame data structure.
  - {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`
* - {numref}`slicing-df`
  - **Slicing DataFrames**: This exercise goes over different techniques on how to extract data from DataFrames.
  - {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`
* - {numref}`plotting-pandas`
  - **Plotting Pandas data with Matplotlib**: This exercise shows how to draw plots using the DataFrame data.
  - {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`
* - {numref}`highlight_scatter`
  - **Highlighting points in a scatter plot**: In this exercise we highlight a subset of points in a different colour.
  - {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`
* - {numref}`create-columns`
  - **Creating new columns**: In this exercise, we use existing column data to derive new ones.
  - {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`
* - {numref}`save-df-file`
  - **Saving data into files**: In this exercise, we will save DataFrame data into a tab-delimited file.
  - {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`
* - {numref}`split-apply-combine-ex`
  - **Split-apply-combine**: In this exercise, we will be using the split-apply-combine appraoch to apply functions of grouped data.
  - {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`
* - {numref}`independent-programmer`
  - **Moving on beyond the course**: In the exercise, we will explore resources on how we can explore further functionality in packages to help us solve our computational problems.
  - {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning`
```

:::{card} Managed to solve all the exercises?  Well done!
:class-card: sd-bg-light
In the programming world, many organisations award badges to learners on the acquisition of a new skill or completion of a milestone.  If you attempted and solved all the exercises of this practical, you definitely deserve your final badge of the Python practicals!
```{image} images/level-3-badge.png
:name: level3-badge
:width: 20%
:align: center
```
:::


```{admonition} Next steps
To be profecient in a programming language you need to practice a lot!

After the course:
 * go over the notes again and make sure you know the core concepts introduced in this course.  
 * follow this by looking into other online resources to practice more python, for example, you should have free access to [Linked-in learning](http://www.cam.ac.uk/linkedinlearning) as a member of the Univeristy of Cambridge, 
 a resource with many tutorials and courses.
 * the upcoming lectures and practicals will continue to introduce you to ways on how you can explore biological data with Python.
 
Happy Python practicing!
```







