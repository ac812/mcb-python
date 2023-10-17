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

# Debugging code in PyCharm

This process fixing errors in code is known as **debugging**.  A software **bug** in an error in your code that makes your program stop or not run as it should be. 
Debugging your code can also be useful when you want to understand properly what your code is doing.  PyCharm offers a really useful tool - the **PyCharm debugger**. 
The PyCharm debugger allows you to execute your code one line at a time, and also help you understand how the values of your variables are changing in memory.

To debug your code you must first create a **breakpoint**, by clicking in the gutter in PyCharm:

```{figure} images/breakpoint.png
---
name: breakpoint
---
A breakpoint on line 7 in PyCharm.
```

As shown in {numref}`breakpoint`, the red dot, is the breakpoint.  Next, click on the Debug ![](images/debug.png) button.  The code will start executing util it reaches the first breakpoint which essentially 
pauses the code from executing, allowing you to see the values of the variables at that point.  In 
the example below, we can see that when the code pauses execution on line 7, `i` has the value of 0, `rows` 5 and `spaces` 4 in the 
Debug tool window.  These values are also shown inline next to the code (inline debugger).

```{figure} images/debug-tool.png
---
name: debug-tool
---
Debug tool window in PyCharm
```

To run one line of code at a time, press the Step Over ![](images/step-over.png) button. This is 
very useful as it allows you to check what is happening in your code, especially if you are trying to fix an 
error in your code.  You can put as many breakpoints as you want in your code.  Pressing the Resume Program ![](images/resume-program.png) button 
will resume execution of program until the next breakpoint is reached.  Pressing the Stop ![](images/stop.png) button will stop execution of your program.

````{admonition} Do you know?
:class: tip

The term **bug** was first used in 1946 by **Grace Hopper**, a computer science pioneer.  A moth was trapped in a relay, which caused a malfunction in the 
electricalmechanical computer leading eventually to the word "bug" to refer to errors in code.
 
```{figure} images/grace-hopper.jpeg
Grace Hopper ([Wikipedia](https://commons.wikimedia.org/wiki/File:Grace_Hopper_and_UNIVAC.jpg))
```
````





