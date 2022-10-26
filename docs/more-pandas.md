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

# More Pandas

## Create a new column
Similar to NumPy, Pandas supports vectorised operations.  This means, that we do not need to create loops to 
perform basic element-wise operations.  In the example below, we create a new column `population_p`, that takes the values 
of column `population_t` and divides them by the values of column `land_area`.

```{code-cell} ipython3
:tags: [output_scroll]

import pandas as pd

# read data from file
df = pd.read_csv("data/world-bank-1_data.csv")

# check the size of the DataFrame
print(df.shape)

# calculate the population density
df["population_d"] = df["population_t"]/df["land_area"]

# check the size of the DataFrame again
print(df.shape)

# check the first few rows
df.head()
```

Similarly, other mathematical operators can be used to perform other arithmethic operations on columns.

```{exercise-start} Create columns
:label: create-columns
```
**Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`

Using the `df` DataFrame object created above, create the following new columns:
1. fraction of male population (population_m_f)
2. fraction of female population (population_f_f)

```{exercise-end}
```


[//]: # (## Renaming columns)


## Writing data to files
Now that we have made changes to our dataset, let us save it in a file so that we keep it safe.  To save our dataset into a 
.csv format the [`to_csv()` method](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html?highlight=to_csv#pandas.DataFrame.to_csv) is used.

```{code-cell} ipython
df.to_csv("data/world-bank-1m_data.csv")
```

In the code above, the `to_csv()`method is saving the data that is currently present in `df` into a file called `world-bank-1m_data.csv` 
in the `data` folder.  There are other file formats that DataFrames can be saved into.  They normally have the format of `to_*`. Look 
into [Pandas documentation](https://pandas.pydata.org/docs/reference/frame.html#serialization-io-conversion) for a whole list.

```{exercise-start} Saving data into files
:label: save-df-file
```
**Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`

Perform the following:
1. Save the `df` DataFrame into a tab-delimited .txt file in the data folder with the name world-bank-1_data.txt. 
2. Check the file has been created and open it to verify that it is tab-delimited.
3. Read the file back into Python into a new DataFrame object (df2) and check that the data has loaded well.

```{exercise-end}
```

## Handling missing data

Missing data in Pandas is displayed as `nan`.  In practice, if we are compiling a dataset ourselves, we should keep the 
respective data item empty so that the dataset can be used by different programming languages and systems.  

One useful operation is to remove all rows that have an `nan` in them (even if it is just in one column).  This can be done 
by using the `dropna()` method.

```{code-cell} ipython3
print(f"Size of df is: {df.shape}")

df_complete = df.dropna()

print(f"Size of df_complete is: {df_complete.shape}")
```

When dealing with data something you might also want to detect missing values in a column rather than the whole dataset. 
The `isna()` function returns a Series of `True` and `False` depending on whether the data item in the Series is `nan` or not.
The `notna()` function does the opposite of `isna()`, it returns `False` if the respective data item in the Series is `nan`, and 
`True` if a value is present.

```{code-cell} ipython3
:tags: [output_scroll]

# Aruba does not seems to have co2 emissions data
aruba_data = df[df["country"] == "Aruba"]

co2_emissions_isna = pd.isna(aruba_data["co2_emissions_pc"])
print(co2_emissions_isna)

co2_emissions_notna = pd.notna(aruba_data["co2_emissions_pc"])
print(co2_emissions_notna)
```

[//]: # (## joining data frames)

[//]: # ()
[//]: # (## pivot)

[//]: # ()
[//]: # (## sort data in a dataframe)

[//]: # (which of the countries has the highest life expectancy)

[//]: # ()
[//]: # (## group by - split apply combine)





