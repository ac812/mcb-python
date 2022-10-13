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


# `NumPy` 

## What is Numpy?
Package

## Differences between NumPy arrays and standard Python sequences (e.g., lists)
Table on column numpy the other lists
https://numpy.org/devdocs/user/whatisnumpy.html


### Advantages over lists

* NumPy uses a **vectorised** code system for arrays so no need to use loops to apply operations on each data item. It facilitates mathematical and other operations on data structures:
    * Fewer lines of code
    * Easier to read, resembles mathematical notation.

`````{tab-set}
````{tab-item} Standard Python
```{code-block}
c = []
for i in range(len(a)):
    c.append(a[i]*b[i])
```

````

````{tab-item} NumPy
```{code-block}
c = a * b
```
````
`````

* <Fast
benchmark example above>



[//]: # (#```{admonition})

[//]: # (#:class: tip)

[//]: # ()
[//]: # (#Timing of numpy versus normal list)

[//]: # ()
[//]: # (#`````)


Because we are using the Anaconda distribution, numpy should be already installed in our system.  You can check this in the Python Packages tab
in PyCharm.  
However to use numpy functions we need to import it in the code.  The widely adopted convention is as follows:

```{code-cell} ipython3
import numpy as np
```



