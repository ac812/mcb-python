# Modules and Packages

:::{card} Modules and Packages
:class-card: sd-bg-light

{bdg-info}`Programming concept`

A **module** is a collection of functions.

A **package** is a collection of modules. 
:::

The functions we have used so far are available in the **Python Standard Library**, which means they come automatically as part of your
Python distribution.  One can also have access to additional functions that are not part of the Python standard library which will 
provide us with more features that we can use in Python, such as creating plots.  To do this we would need to **import modules** into our Python code.

`import` statements are normally placed as the first lines of code in your file, before the other code. The syntax to import modules is as follows:

**`import` *module_name*   
`import` *package_name*`.`*module_name*  
`import` *module_name* `as` *preferred_name*  
`import` *package_name*`.`*module_name* `as` *preferred_name*  
`from` *package_name* `import` *module_name* `as` *preferred_name***  

The third, fourth and fifth example, allows us to specify an alias or alternative name of our choosing to refer to the module. 
In choosing this *preferred_name* we need to be careful of name clashes with existing keywords, functions or variables. 
Once a module is imported, we would be able to access all the functions of this module in our code.  Assuming our example module above 
contains a function called `fun1()`, after importing the module we can call `fun1()` from our code as 
following:

***module_name*.`fun1()`** or ***preferred_name*`.fun1()`** if a *preferred_name* was specified when importing the module.  

In this course we will be looking into importing modules from two popular packages; `matplotlib` and `numpy`.


