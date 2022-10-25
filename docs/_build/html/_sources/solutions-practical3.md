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
df[df["country"] == "United Kingdom" & df["year"] == 2020]
```
```{solution-end}
```


