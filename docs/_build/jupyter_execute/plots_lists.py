#!/usr/bin/env python
# coding: utf-8

# # Getting started with Matplotlib
# 
# In this section we are going to get started with drawing plots from lists using the `matplotlib` package. 
# `matplotlib` is the most widely used package for visualising data in Python [^python-survey].
# 
# 
# ## Importing Matplotlib
# Like NumPy Matplotlib should also be present in the Anaconda distribution (check the Python Packages tab in PyCharm).
# 
# To import matplotlib in your code use the following code:

# In[1]:


import matplotlib.pyplot as plt


# ## Drawing our first plot
# 
# Let us start by drawing a simple line plot:

# In[2]:


import matplotlib.pyplot as plt

# values of x and y points

x = [1, 2, 3, 4, 5]
y = [2, 3, 4, 5, 6]

plt.plot(x, y)
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()


# In the code above, `x` and `y` represent the coordinates to plot on our plot.  The `plot()` function takes as an argument 
# the x and y coordinates to plot (see [documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)).
# `plt.xlabel()` sets the title of the x-axis label, and similarly `plt.ylabel()` sets the title of the y-axis label. 
# Calling `plt.plot(x,y)` on its own will not plot the plot for us. To visualise the plot we need to call the `plt.show()` function.
# 
# When you run the code above in PyCharm you can see the output of this plot in the SciView tool window on the right hand side in the 
# Plots view.
# 
# ```{figure} images/plots-view-pycharm.png
# ---
# name: plots-view-pycharm
# width: 50%
# ---
# Plot displayed in PyCharm in the SciView tool window | Plots view.
# ```
# If this is not visible click *View > Scientific mode* from PyCharm's menu to enable it.
# 
# You can also use `plt.plot()` to plot markers on the plot.  To do this you need to use the `fmt` parameter 
# that takes as an input a format string that specifies the type of marker you want to plot.  The syntax of the format string
# originates from MATLAB which concatenates a colour string with a line style string.  The code below shows an example of plotting 
# the same (x,y) coordinates in the previous plot but this time using red circle markers:

# In[3]:


import matplotlib.pyplot as plt

x = [2, 3, 4, 5, 6]
y = [1, 2, 3, 4, 5]

plt.plot(y, x, "ro")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()


# There is a vast list of string formats you can specify that generate different markers.  A whole list of format strings supported can be found [here](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html) at the bottom 
# of the page in the **Notes** section.  
# 
# ```{exercise-start} Draw dotted line plot with markers
# :label: line-plot
# ```
# 
# **Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`
# 
# ```{code-block}
# x = [2, 3, 4, 5, 6]
# y = [1, 2, 3, 4, 5]
# ```
# Using the `x` and `y` coordinates above, draw a plot with green circle markers joined together with a dashed line as shown below.  The plot should 
# look like this:
# ```{image} images/green-dotted-plot.png
# :width: 60%
# ```
# ```{exercise-end}
# ```
# 
# `plt.plot()` is only used to plot x and y coordinates as lines or markers.  If you want to plot something else, you need to use 
# a different plot.  You can see a list of the different plots supported in Matplotlib [here](https://matplotlib.org/stable/plot_types/index.html). 
# 
# ```{exercise} Plotting a scatter plot
# :label: scatter-plot
# 
# **Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`
# 
# Generate 20 random numbers from 0 to 1, and set these as your x and y values.  Plot these on a scatter plot.
# 
# ```
# 
# 
# This section was a gentle introduction, we will be plotting more with Matplotlib in next week's practical.  
# 
# [^python-survey]: [Python Developers Survey](https://lp.jetbrains.com/python-developers-survey-2021/)
