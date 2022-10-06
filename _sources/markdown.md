
These notes will teach you how to code in Python and how to work with the PyCharm IDE.

Please install Python and PyCharm following [these instructions](installation). 

[Here](intro-to-python) are some instructions to get you started coding in Python using PyCharm.  

## Sample Roles and Directives

Roles and directives are two of the most powerful tools in Jupyter Book. They
are kind of like functions, but written in a markup language. They both
serve a similar purpose, but **roles are written in one line**, whereas
**directives span many lines**. They both accept different kinds of inputs,
and what they do with those inputs depends on the specific role or directive
that is being called.

Here is a "note" directive:

```{note}
Here is a note
```

It will be rendered in a special box when you build your book.

Here is an inline directive to refer to a document: {doc}`markdown-notebooks`.


## Citations

You can also cite references that are stored in a `bibtex` file. For example,
the following syntax: `` {cite}`holdgraf_evidence_2014` `` will render like
this: {cite}`holdgraf_evidence_2014`.

Moreover, you can insert a bibliography into your page with this syntax:
The `{bibliography}` directive must be used for all the `{cite}` roles to
render properly.
For example, if the references for your book are stored in `references.bib`,
then the bibliography is inserted with:

```{bibliography}
```

## Learn more

This is just a simple starter to get you started.
You can learn a lot more at [jupyterbook.org](https://jupyterbook.org).


```{note}
:class: dropdown
The note body will be hidden!
```


"attention", "caution", "danger", "error", "hint", "important", "note", "tip", "warning"
<img alt="Mozilla Add-on" src="https://img.shields.io/amo/stars/alex?label=level">
https://sphinx-book-theme.readthedocs.io/en/latest/reference/kitchen-sink/admonitions.html
![Mozilla Add-on](https://img.shields.io/amo/stars/dustman?label=level&style=for-the-badge)
```{admonition} Exercise
:class: important, dropdown
Here's what's inside!
```
<img alt="Mozilla Add-on" src="https://img.shields.io/amo/stars/alex?label=level">

```{exercise}
:class: dropdown, space, style="margin-top:0px"

Recall that $n!$ is read as "$n$ factorial" and defined as
$n! = n \times (n - 1) \times \cdots \times 2 \times 1$.

There are functions to compute this in various modules, but let's
write our own version as an exercise.

In particular, write a function `factorial` such that `factorial(n)` returns $n!$
for any positive integer $n$.
```
<img alt="Mozilla Add-on" src="https://img.shields.io/amo/stars/alex?label=level">

```{admonition} Extra credit
Testing new admonition.
```
````{card}
{bdg-primary}`example-badge`

Content of the top card.
````

```{tableofcontents}
```


```{list-table} Common data-types in Python
:header-rows: 1
:name: data-types-table

* - Data Type
  - Description
  - Example
* - int
  - Integers (whole numbers)
  - 40
* - float
  - Numbers with decimal points (default)
* - Decimal
  - Numbers with decimal points (high precision)
* - str
  - Strings; sequence of characters
  - "Hello World!"
* - bool
  - Boolean; can only be `True` or `False`
  - t
```



```{code-cell} iphython3
#This program will print Hello World!
print("Hello", "World!")
```
