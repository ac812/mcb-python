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

# Control flow statements

As the name suggests, control flow statements are statements that control the order of which code is executed in a program.
In this section we will be looking at different forms of control flow statements.  

## `if` statements

The `if` statement is used to execute a piece of code based on a condition.  {numref}`if` shows the syntax of the `if` 
statement together with its representation in a flow chart.  

```{figure} images/if.png
---
name: if
---
Syntax of `if` statement (*A*) together with a flowchart representation (*B*).
```
where *expression1* and *expression2* are boolean expressions and *suite1,suite2,suite3* refer to one or more statements. The `elif` and `else` 
parts of the `if` statement are optional. `elif` is short for "else if".  Essentially, if *expression1* evaluates to `True`, 
the code in the `if` branch is executed (*suite1*), otherwise if *expression2* evaluates to `True`, the code in the `elif` branch 
is executed (*suite2*), otherwise the code in the `else` branch is executed (*suite3*).

(code-reference-marking)= 
```{code-cell} ipython3
total_mark = 50

#check which class total_mark falls in and print it
if total_mark > 69:
    print("First")
elif total_mark > 49:
    print("Second")
elif total_mark > 39:
    print("Third")
else:
    print("Fail")
```

```{admonition} Note: Code Indentation
Python uses indentation to specify blocks of code.  To indent code use **4 spaces** per indentation level (not a tab). PyCharm 
will indent your code automatically when you press a new line after an `if` statement. Writing the code above without 
indentation will throw an error.
```


```{exercise} Month in number
:label: month-if

**Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`
  
Write a program where given a month in number format as an input, it will print that month's name back.  For example, month = 10
will print October.
```

## `match` Statements
When you need to compare the value of a variable to several patterns, using `match` statements is more useful. It is 
more used with string comparisons rather ones since it has to match the values.  The code below is a good example of when 
it is better to use `match` rather than `if` statements.  The code below prints "Hello" in the language you specify.
```{code-cell} ipython3
language = "English"

#print hello depending on what language is specified
match language:
    case "English":
        print("Hello")
    case "French":
        print("Bonjour")
    case "Italian":
        print("Salve")
    case "Portuguese":
        print("Ola")
    case "Maltese":
        print("Bonġu")
    case "Chinese":
        print("Nǐn hǎo")
    case "Maasai":
        print("Sopa")
    case _:
        print("Language not supported yet")
```
The case where there is a match is executed.  The last `case`, `_` is a wildcard, which means that if none of the cases match, 
that case will be executed.  


```{exercise} Month in number v2.
:label: month-match

**Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`
  
Write the same program as {numref}`month-if` but use the `match` statement this time to specify conditions.
```

So far we have compared single values, what if we want to compare a value to a list?  For example, checking if the `int` values in 
a list are more than 20.

```{code-cell} ipython3
:tags: ["raises-exception"]

l = [55, 92, 110, 66, 75, 45, 40, 57, 55, 62]

l > 20
```
As you can see this will throw an error as this code is trying to compare a `list` object to an `int` object.  What we 
really want to do is check if the value of each `int` object in list `l` is greater than 20.  In this way, both the left and right-hand 
side of the comparison operator will be of the same value (`int` in this example).  To do this we have to use loops.

## Loops
Loops form also part of control flow statements.  They are the tool needed to **repeat** operations until a defined condition 
is reached.  In the next sections we will look at the `while` and `for` loops.  

### `for` loop
Python’s `for` statement (or **`for` loop**) iterates over the items of a sequence (*e.g.,* string, tuple, list). 
{numref}`for` below shows the syntax of a `for` loop together with a flowchart.

```{figure} images/for.png
---
name: for
---
Syntax of `for` loop (*A*) together with a flowchart representation (*B*)
```

The way `for` loops work is better explained by the animation below which shows how the code in the left-hand side of 
the animation is executed.  

```{figure} images/for-loop.gif
---
name: for-loop
---
Animation demo of `for` loop example 
```
As shown in the animation in {numref}`for-loop`, the `for` loop continues to iterate over each item in list `x` until the end of the list is reached. 
The value of item `i` in the example code is initialised after each iteration.  This means that the code below will not 
advance the item to be retrieved from list `x`.

```{code-cell} ipython3
x = [10, 20, 30]

for i in x:
    print(i)
    i = i + 5
```

````{exercise} for loop
:label: for-exercise
**Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`

Print the following list one word on a new line using a `for` loop.

```{code-block}
l = ["keep", "calm", "and", "carry", "on"]
````

#### `range()` function
To repeat an operation for $n$ times, `range()` is very useful, especially if $n$ is a large number.  Range generates numbers 
in a range.  

```{list-table} range() function arguments
:header-rows: 1
:name: range

* - Input
  - Description
  - Example
* - `range(`stop`)`
  - Generates a sequence of numbers from *0* to *stop*, excluding the number *stop*.
  - `range(5)` will generate numbers `0,1,2,3,4`
* - `range(`start``, ``stop`)`
  - Generates a sequence of numbers from *start* to *stop*, excluding the number *stop*.
  - `range(3,7)` will generate numbers `3,4,5,6`
* - `range(`start`, `stop`, `step`)`
  - Generates a sequence of numbers that contains the *step<sup>th</sup>* item from the sequence starting from the *start* number to the *stop* number, excluding the *stop* number.
  - `range(0,10,3)` will generate numbers `0,3,6,9`
```

````{Note}
The output from `range()` is not a list, it is actually a `range` object which is an **iterable**, which means, it is able 
to return its data items one at a time.  `range` is a very efficient way of storing sequential numbers in Python as it 
always takes the same amount of memory, no matter the size of the numeric sequence.  For example, `range(5)` and `range(100000)` will
still take the same amount of memory as 'range()' only stores the *start*, *stop* and *step* of the sequence.  


To look at the numbers generated by `range()`, convert `range` to a list as shown below. 

```{code-block} 
# printing range directly will not show you the full sequence of numbers generated
print(range(5))   #prints range(0, 5)

# you need to convert it to a list first
print(list(range(5)) #prints [0, 1, 2, 3, 4]

#since range is an iterable you can use it in functions that take iterable as an input, example:
sum(range(5))  # returns the sum of 0 + 1 + 2 + 3 + 4
```
````

```{exercise} Range
:label: range-exercise
**Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`

In this exercise we are going to explore the `range()` function.
1. Try the code in {numref}`range`.  
2. Use the `for` loop and `range()` function to print *"Hello World!"* three times.
```

#### `break`
The `break` statement exits (or breaks) from the execution of the respective loop code, that is, it does not continue executing the code in the 
current loop. The code below is an example of how to `break` a for loop.  The code prints each character of the string 
"supercalifragilisticexpialidocious" until the first character "c" is met.

(code-break)=
```{code-cell} ipython3
for letter in "supercalifragilisticexpialidocious":  #1
   if letter == 'c':                                 #2
      break                                          #3
   print('Current Letter :', letter)                 #4 
                                                     #5
print("I am now outside of the for loop")            #6
```

The `print` statement in line 4 is at the same indentation as the `if` statement in line 2, meaning that both should run in the 
same iteration of the loop.  However, in the iteration when `letter` is "c", the code inside the `if` statement is executed first, which breaks the loop and thus 
the remaining code in the loop is not executed (skipped).  Note also, that the `print` statement in line 6 is not indented under the `for`
loop, and thus it does not form part of the code in the loop (it is outside the loop).

#### `continue`

The `continue` statement will skip the remaining code in the current iteration, but it will continue the execution of the 
remaining iterations of the loop.  The code below is an example of how to `continue` a loop.  The code goes over a list of 
consecutive numbers from 0 to 9 and identifies even and odd numbers.

(code-continue)=
```{code-cell} ipython3
for i in range(10):                #1
    if i % 2 == 0:                 #2
        print("Even number:", i)   #3
        continue                   #4
    print("Odd number: ", i)       #5
```
In line 2, if the remainder of `i % 2` is 0, the even number is first printed (line 3), then `continue` will skip the remaining 
lines in the loop (line 5) and continue looping over the next iterations until `i` is 10.

```{exercise} break and continue
:label: break-continue
**Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`

In this exercise we will explore the `break` and `continue` statements in loops.
1. Using the code in the [break example](code-break), what happens if you print the current letter in the loop before the 
`if` statement? Why do you think that happened?
2. Remove `continue` (line 4) in the [continue example above](code-continue).  What happens?  Why do you think this has happened? 
```


### `while` loop
The `while` statement executes code that is indented under it until a condition is `True`. 
In {numref}`while-loop` below, *suite* (one or more statements) will continue to execute until *expression* is `True`.

```{figure} images/while.png
---
name: while-loop
---
Syntax of `while` loop (*A*) together with a flowchart representation (*B*)
```

The animation below runs the code on the left hand side of the animation.  It iterates over the `while` loop to explain 
how a `while` loop works.

```{figure} images/while-loop.gif
---
name: anim-while-loop
---
Animation demo of `while` loop example
```

As shown in the animation above, the `while` loop does not iterate over a sequence (as was the case of the `for` loop).  In this example, 
`i` is incremented via the suite of the loop `i += 1` which increments `i` in each iteration.  The `break` and `continue` statements 
can also be used inside the `while` loop.

````{exercise} Numbers program
:label: num-prog
**Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning`  {octicon}`star;1em;sd-text-warning`

Write a program that allows a user to enter numbers.  If the user inputs -1, the program will quit.

```{tip}
The `input()` function takes the user's input as a string.  This will allow for interaction from the user. 
```
````

````{exercise} Fibonacci sequence
:label: fibonacci

**Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning`

Write code that creates a Fibonacci sequence, where the last number of the series is not more than 100.
The Fibonacci sequence is a sequence of numbers where each number is the sum of the two numbers preceding it.   You can 
read more about it [here](https://en.wikipedia.org/wiki/Fibonacci_number)
```{tip}
$F_{0} = 0$ , $F_{1} = 1,$  
and  
$F{n} = F_{n-1} + F_{n-2}$
```
````


