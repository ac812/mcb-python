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

# Practical 3 Solutions

```{solution-start} matrix-manip-exercise
:label: matrix-manip-exercise-solution
:class: dropdown
```
2., 
```{code-cell} ipython3
import numpy as np

m = np.array([[8, 2, 3], [2, 3, 4], [4, 8, 9]])

print(-np.sort(-m, 1))
```

3.a.,
```{code-cell} ipython3
#get the frequency of each value in the array
unique, count = np.unique(m, return_counts=True)
# unique values
print(unique)
# frequency of these unique values
print(count)
```

3.b.,
```{code-cell} ipython3
#get the index position of the first occuring unique value
unique, indices = np.unique(m, return_index=True)
#unique values
print(unique)
# index positions of first occuring unique values
print(indices)
```

```{solution-end}
```


```{solution-start} shaping-matrix
:label: shaping-matrix-solution
:class: dropdown
```

```{code-cell} ipython3
a = np.arange(8)
m = a.reshape(4, 2)
print(m)

```

```{solution-end}
```

```{solution-start} sum-columns-matrix
:label: sum-columns-matrix-solution
:class: dropdown
```
```{code-cell} ipython3
print(np.sum(m, axis = 0))
```

```{solution-end}
```

```{solution-start} exploring-df
:label: exploring-df-solution
:class: dropdown
```
1. `df` is a DataFrame object.  One of the ways you could get this is via the `type` function:
```{code-cell} ipython3
import pandas as pd

df = pd.read_csv("data/world-bank-1_data.csv")
type(df)
```
2., 

```{code-cell} ipython3
# this returns a tuple in the format of (number of rows, number of columns)
df.shape
```

3., 
```{code-cell} ipython3
df.dtypes
```

```{solution-end}
```

```{solution-start} slicing-df
:label: slicing-df-solution
:class: dropdown
```
1.
```{code-cell} ipython3
:tags: [output_scroll]
df.iloc[ : , 0:3]
```
2.,
```{code-cell} ipython3
:tags: [output_scroll]
df.iloc[0:3]
```

3.,
```{code-cell} ipython3
:tags: [output_scroll]
df.iloc[0]
```
4.,
```{code-cell} ipython3
:tags: [output_scroll]
#get min and max values of life_expectancy_max
le_min = df["life_expectancy_t"].min()
le_max = df["life_expectancy_t"].max()

# get country with lowest life expectancy
df.loc[df["life_expectancy_t"] == le_min, "country"]

# get country with highest life expectancy
df.loc[df["life_expectancy_t"] == le_max, "country"]
```
5.,
```{code-cell} ipython3
:tags: [output_scroll, "raises-exception"]

uk_data = df[df["country"] == "United Kingdom"]

# get number of rows and columns from DataFrame - 14 records were returned
uk_data.shape
```
6.,
```{code-cell} ipython3
uk_2020 = df[(df["country"] == "United Kingdom") & (df["year"] == 2020)]

# get number of rows and columns from DataFrame - 1 record was returned
uk_2020.shape
```
7.,
```{code-cell} ipython3
:tags: [output_scroll, "raises-exception"]
df[df["country"] == "United Kingdom" & df["year"] == 2020]
```
```{solution-end}
```


```{solution-start} highlight_scatter
:label: highlight_scatter-solution
:class: dropdown
```

Solution 1:  using plt.subplots().
Here you would have to convert the columns to numpy arrays as you will be using matplotlib functions directly.
```{code-cell}
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
```

Solution 2: using the DataFrame plot functions
```{code-cell}
# extract records where co2_emissions_pc are > 40
highlight = df[df["co2_emissions_pc"] > 40]

ax1 = df.plot.scatter("life_expectancy_t", "co2_emissions_pc")
highlight.plot.scatter("life_expectancy_t", "co2_emissions_pc", color="red", ax=ax1)
plt.show()
```

```{solution-end}
```


```{solution-start} create-columns
:label: create-columns-solution
:class: dropdown
```
```{code-cell} ipython3
df["population_m_f"] = df["population_m"] / df["population_t"]
df["population_f_f"] = df["population_f"] / df["population_t"]
```
```{solution-end}
```

```{solution-start} save-df-file
:label: save-df-file-solution
:class: dropdown
```
1. 
```{code-cell} ipython3
# Pandas does not have a to_txt() function so we need to adapt the to_csv() method.
df.to_csv("data/world-bank-1_data.txt", sep="\t", index=False)
```

3.,
```{code-cell} ipython3
:tags: [output_scroll]
df2 = pd.read_csv("data/world-bank-1_data.txt", sep="\t")
df2.head()
```

```{solution-end}
```


