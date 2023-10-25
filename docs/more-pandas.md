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

## Select-Apply-Combine

So far we have applied operations over all the DataFrame object.  However, in data analysis, especially when dealing with
big data, a common approach to data exploration is the split-apply-combine strategy. The idea behind this strategy is 
to split the data into more managable pieces, apply any operations required on the data independently on each piece and 
then combine the results together. The {numref}`split-apply-combine` below illustrates the approach that is done in the split-apply-combine approach.

```{figure} images/split-apply-combine.png
---
name: split-apply-combine
---
An illustration on how the Split-Apply-Combine strategy works.
```

The code below is the Python version of the Split-Apply-Combine approach.  In this code, we are splitting the `df` DataFrame 
by `year`.  For each `year` records, we are applying the `mean()` function on it.  We are the combining the results from each `year` grouping 
and merging it into one DataFrame which is then stored in the `res` variable.

```{code-cell} ipython3
# for each year, get the average co2 emissions
res = df.groupby("year")["co2_emissions_pc"].mean()
print(res)
```

```{exercise-start} Select-Apply-Combine
:label: split-apply-combine-ex
```
**Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`

Find the maximum value of CO2 emmissions for each country in the `df` DataFrame.

```{exercise-end}
```

```{exercise-start} Becoming an independent programmer
:label: independent-programmer
```
**Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning`

The purpose of this course is to teach you the core concepts well.  It is up to you to then apply these concepts to solve your 
computational/mathematical problems. 

One thing you should be aware of is that popular packages normally have a cheat sheet.  A cheat sheet is a summarised but user-friendly 
version of all the functionality of a package.  You can find the cheat sheet for [pandas here](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf) and 
[Matplotlib here](https://matplotlib.org/cheatsheets/_images/cheatsheets-1.png).

Have a look at the cheat sheet and attempt using a new functionality.

```{note}
The cheat sheet alone is not enough.  To maximise your potential as a programmer you would also need to use the reference documentation 
of each respective package. If you go in the documentation of a function and scroll down to the bottom of the page, you will also see 
exercises that will help you understand better (the sometimes complex) documentation.  
[Link to Matplotlib documentation](https://matplotlib.org/stable/api/index).    
[Link to Pandas documentation](https://pandas.pydata.org/docs/)  

Use the links above to explore the documentation of Matplotlib and Pandas.
```

```{exercise-end}
```


[//]: # (## joining data frames)

[//]: # ()
[//]: # (## pivot)

[//]: # ()
[//]: # (## sort data in a dataframe)

[//]: # (which of the countries has the highest life expectancy)





