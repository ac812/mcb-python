#!/usr/bin/env python
# coding: utf-8

# # Practical 3 Solutions
# 
# ```{solution-start} matrix-manip-exercise
# :label: matrix-manip-exercise-solution
# :class: dropdown
# ```
# 2.,

# In[1]:


import numpy as np

m = np.array([[8, 2, 3], [2, 3, 4], [4, 8, 9]])

print(-np.sort(-m, 1))


# 3.a.,

# In[2]:


#get the frequency of each value in the array
unique, count = np.unique(m, return_counts=True)
# unique values
print(unique)
# frequency of these unique values
print(count)


# 3.b.,

# In[3]:


#get the index position of the first occuring unique value
unique, indices = np.unique(m, return_index=True)
#unique values
print(unique)
# index positions of first occuring unique values
print(indices)


# ```{solution-end}
# ```
# 
# 
# ```{solution-start} shaping-matrix
# :label: shaping-matrix-solution
# :class: dropdown
# ```

# In[4]:


a = np.arange(8)
m = a.reshape(4, 2)
print(m)


# ```{solution-end}
# ```
# 
# ```{solution-start} sum-columns-matrix
# :label: sum-columns-matrix-solution
# :class: dropdown
# ```

# In[5]:


print(np.sum(m, axis = 0))


# ```{solution-end}
# ```
# 
# ```{solution-start} exploring-df
# :label: exploring-df-solution
# :class: dropdown
# ```
# 1. `df` is a DataFrame object.  One of the ways you could get this is via the `type` function:

# In[6]:


import pandas as pd

df = pd.read_csv("data/world-bank-1_data.csv")
type(df)


# 2.,

# In[7]:


# this returns a tuple in the format of (number of rows, number of columns)
df.shape


# 3.,

# In[8]:


df.dtypes


# ```{solution-end}
# ```
# 
# ```{solution-start} slicing-df
# :label: slicing-df-solution
# :class: dropdown
# ```
# 1.

# In[9]:


df.iloc[ : , 0:3]


# 2.,

# In[10]:


df.iloc[0:3]


# 3.,

# In[11]:


df.iloc[0]


# 4.,

# In[12]:


#get min and max values of life_expectancy_max
le_min = df["life_expectancy_t"].min()
le_max = df["life_expectancy_t"].max()

# get country with lowest life expectancy
df.loc[df["life_expectancy_t"] == le_min, "country"]

# get country with highest life expectancy
df.loc[df["life_expectancy_t"] == le_max, "country"]


# 5.,

# In[13]:


uk_data = df[df["country"] == "United Kingdom"]

# get number of rows and columns from DataFrame - 14 records were returned
uk_data.shape


# 6.,

# In[14]:


uk_2020 = df[(df["country"] == "United Kingdom") & (df["year"] == 2020)]

# get number of rows and columns from DataFrame - 1 record was returned
uk_2020.shape


# 7.,

# In[15]:


df[df["country"] == "United Kingdom" & df["year"] == 2020]


# ```{solution-end}
# ```
# 
# 
# ```{solution-start} highlight_scatter
# :label: highlight_scatter-solution
# :class: dropdown
# ```

# In[16]:


import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# extract records where co2_emissions_pc are > 40
highlight = df[df["co2_emissions_pc"] > 40]

# extract columns to represent x and y axis for plot
x = df["life_expectancy_t"].to_numpy()
y = df["co2_emissions_pc"].to_numpy()
x_highlight = highlight["life_expectancy_t"].to_numpy()
y_highlight = highlight["co2_emissions_pc"].to_numpy()

# first plot all the points as black points
ax.scatter(x, y, c="black")

#the plot the points present in highlight in red
ax.scatter(x_highlight, y_highlight, c="red")

fig.show()


# ```{solution-end}
# ```
# 
# 
# ```{solution-start} create-columns
# :label: create-columns-solution
# :class: dropdown
# ```

# In[17]:


df["population_m_f"] = df["population_m"] / df["population_t"]
df["population_f_f"] = df["population_f"] / df["population_t"]


# ```{solution-end}
# ```
# 
# ```{solution-start} save-df-file
# :label: save-df-file-solution
# :class: dropdown
# ```
# 1.

# In[18]:


# Pandas does not have a to_txt() function so we need to adapt the to_csv() method.
df.to_csv("data/world-bank-1_data.txt", sep="\t", index=False)


# 3.,

# In[19]:


df2 = pd.read_csv("data/world-bank-1_data.txt", sep="\t")
df2.head()


# ```{solution-end}
# ```
