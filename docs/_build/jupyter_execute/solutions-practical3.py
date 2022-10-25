#!/usr/bin/env python
# coding: utf-8

# # Practical 3 Solutions
# 
# ```{solution-start} exploring-df
# :label: exploring-df-solution
# :class: dropdown
# ```
# 1. `df` is a DataFrame object.  One of the ways you could get this is via the `type` function:

# In[1]:


import pandas as pd

df = pd.read_csv("data/world-bank-1_data.csv")
type(df)


# 2.,

# In[2]:


# this returns a tuple in the format of (number of rows, number of columns)
df.shape


# 3.,

# In[3]:


df.dtypes


# ```{solution-end}
# ```
# 
# ```{solution-start} slicing-df
# ```
# 1.

# In[4]:


df.iloc[ : , 0:3]


# 2.,

# In[5]:


df.iloc[0:3]


# 3.,

# In[6]:


df.iloc[0]


# 4.,

# In[7]:


#get min and max values of life_expectancy_max
le_min = df["life_expectancy_t"].min()
le_max = df["life_expectancy_t"].max()

# get country with lowest life expectancy
df.loc[df["life_expectancy_t"] == le_min, "country"]

# get country with highest life expectancy
df.loc[df["life_expectancy_t"] == le_max, "country"]


# 5.,

# In[8]:


uk_data = df[df["country"] == "United Kingdom"]

# get number of rows and columns from DataFrame - 14 records were returned
uk_data.shape


# 6.,

# In[9]:


uk_2020 = df[(df["country"] == "United Kingdom") & (df["year"] == 2020)]

# get number of rows and columns from DataFrame - 1 record was returned
uk_2020.shape


# 7.,

# In[10]:


df[df["country"] == "United Kingdom" & df["year"] == 2020]


# ```{solution-end}
# ```
