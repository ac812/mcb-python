#!/usr/bin/env python
# coding: utf-8

# # Visualising data with Matplotlib
# 
# Now that we have learned how to slice our data let us start visualising it.  We have already seen [previously](plots_lists.md) 
# how to plot simple plots.  Here we will be looking at more examples of how to visualise data with `matplotlib`.
# 
# ## Visualising Pandas data structures in Matplotlib
# The authors of Matplotlib recommend that NumPy arrays are used as an input to Matplotlib functions. They also mention 
# that if Pandas data structures are used, it might not work as intended and therefore recommend to convert these to
# NumPy arrays before plotting [^refmatplotlib].
# 
# Let us start by plotting one of the columns from our DataFrame as a line plot:

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt

# read data from file to DataFrame 
df = pd.read_csv("data/world-bank-1_data.csv")

#plot life expectancy
df["life_expectancy_t"].plot()
plt.show()


# [//]: # (## Saving image to file)
# 
# 
# [^refmatplotlib]: [Matplotlib guide](https://matplotlib.org/stable/tutorials/introductory/quick_start.html#types-of-inputs-to-plotting-functions)
