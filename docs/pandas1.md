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

# Pandas 

## What is Pandas?
Pandas is a Python package designed for data manipulation and analysis. Its name is derived from "**pan**el **da**ta" (not the bear!) and is also 
from "Python data analysis" [^ McKinney]. It is especially popular for its data structures that help process tabular data 
in a fast and efficient way. 

## Importing Pandas

You can check whether Pandas is installed from the *Python Packages* tab in PyCharm.  If it is not, you would see an **install** 
button on the right hand side of the Python Packages pane when you search for Pandas.  Click on the *install* button if 
Pandas is not installed on your machine.
![python-packages](images/pandas-install.png)

To be able to work with Pandas we need to import the Pandas package into our Python code.  Below is the community agreed convention:

```{code-cell} ipython3
import pandas as pd
```

## The dataset

For this session we will be using data from the World Bank Data Catalog [^world-bank] from the World Development Indicators (WDI) collection 
which was transformed by Alexia Cardona for the purpose of teaching data manipulation and visualisation programming. This data is 
compiled using official international resources.

Download the dataset from [here](data/world-bank-1_data.csv) and save it into a `data` folder in your PyCharm project. 

This dataset contains official data for each country worldwide and contains indicators on life expectancy, population, and CO2 emissions.  Below is 
the metadata of the dataset:

```{list-table} Dataset Metadata
:header-rows: 1
:name: ndarray-manip-table

* - Column name
  - Description
* - `country`
  - Name of country.
* - `year`
  - Year data is representative of.
* - `life_expectancy_f`
  - Life expectancy at birth, female (years). Life expectancy at birth indicates the number of years a newborn infant would live if prevailing patterns of mortality at the time of its birth were to stay the same throughout its life.
* - `life_expectancy_m`
  - Life expectancy at birth, male (years).
* - `life_expectancy_t`
  - Life expectancy at birth, total (years).
* - `land_area`
  - Land area (sq. km).
* - `population_m`
  - Male population count.
* - `population_f`
  - Female population count.  
* - `population_t`
  - Total population count.
```

## Reading tabular data from a file

Now that we have everything in place, let us start by first reading our data into our Python code.  Pandas has conventient 
functions that load files containing tabular data.

```{code-cell} ipython3
df = pd.read_csv("data/world-bank-1_data.csv")
```
The code above reads the file `world-bank-1_data.csv` into a `DataFrame` object and creates variable `df` that points to it.
There are other functions in Pandas that read other file formats.  You can see a list of these [here](https://pandas.pydata.org/docs/reference/io.html).
If we run the code above in the Python Console in PyCharm we can see all this information in the Variables pane (see {numref}`dataframe-pycharm`).

```{figure} images/dataframe-pycharm.png
---
name: dataframe-pycharm
---
`df` in the Variables pane in PyCharm.
```

If we click on the *View as DataFrame* link, we can actually see the value of the data that is inside `df`. 
```{figure} images/df-view.png
---
name: df-view
---
Data view of `df` in PyCharm.
```

This is the easiest way to check the data.  Checking the data through the `df` attributes in the Variables pane is not user-friendly 
for DataFrame objects due to the complexity of it. 

## The DataFrame 
The popularity of Pandas mainly lies with its data structure; the `DataFrame`.  The DataFrame data structure is suitable for 
data that is in tabular form (2-dimensional); data with columns and rows.  Since most of the data comes into this form, it makes the DataFrame data structure 
and Pandas widely used.

Now that we have loaded the DataFrame in Python, we need to check if the data has loaded properly.  We already saw how we 
can check this visually via PyCharm.  Let us try to check this in the Console, by printing the first 5 rows of the DataFrame:

```{code-block}
df.head(5)
```
```{code-cell} ipython3
:tags: [output_scroll, remove-input]
    
print(df.head(5))
```

You can also get summary statistics for each column of the `df` DataFrame:

[//]: # (&#40;df.style.set_table_attributes&#40;'style="font-size: 10px"'&#41;&#41;)

```{code-block}
df.describe()
```
```{code-cell} ipython3
:tags: [output_scroll, remove-input]
    
print(df.describe())
```

You can also get a summary of the `dtype` of each column together with the number of non-null values for each column.

```{code-block}
df.info()
```
```{code-cell} ipython3
:tags: [output_scroll, remove-input]
    
print(df.info())
```
Alternatively you can get the `dtype` of each column by using the `dtype` attribute of the DataFrame; `df.dtype`.  Note that
columns which hold string data values are imported into Pandas as `object` `dtype`.


## The Series

Each column in a DataFrame is a Series. 


[//]: # (```{exercise-start} Exploring DataFrames)

[//]: # (```)

[//]: # (In this practical we will be using the dataset from the World Bank Data Catalog.  Follow the instructions above to load the )

[//]: # (dataset into Python.)

[//]: # (1. What type is `df`?)

[//]: # (2. How many columns and how many rows does the `df` have?)

[//]: # (3. What are the data types of each column?)

[//]: # (```{exercise-end})

[//]: # (```)



## Slicing Data Frames


# extract columns - label-based indexing
Selecting a column from the DataFrame object:
df["column_name"] > Series
type(df["life_expactancy_T"])
#get length of Series
life_expectancy.size
size is an attribute not a function - no parentheses

get mutiple columns - takes as an input a standard Python list
df[["column1", "column2",]]  returns a dataframe

# extract rows - boolean indexing
df[conditional expression]
le_top = df[df["life_expectancy_T"] > 80]

# extracting rows and columns - loc/iloc operators
df[R, C]

loc is mainly used with label-based indexing and boolean indexing



# integer-based indexing
iloc is mainly used with  index positions
If you want to use index positions of data, then  use iloc
get the first 10 rows and the first 5 columns
le_top.iloc[0:10, 0:5]

# Modifying the DataFrame
## create a new column

## changing values of existing data
using the loc/iloc operators
le_top.iloc[0:10, 0] = "ABC"
df.loc[df["life_expectancy_t"] > 84, "country"] ="XYZ"

exercise:
1. modify a value
2. check if the original dataset was modified as well. - it should not


## Handling missing data



## joining data frames

## pivot

# sort data in a dataframe

# group by - split apply combine

## writing data to files

## matplotlib

## numpy




[^world-bank]: The World Bank: World Development Indicators Collection.  Terms of Use [here](https://www.worldbank.org/en/about/legal/terms-of-use-for-datasets).  This dataset can also be viewed interactively on the World Data Bank website [here](https://databank.worldbank.org/Teaching-Python-dataset/id/48401a76).
[^ McKinney]: McKinney, Wes (2017). *Python for Data Analysis, Second Edition*.  O'Reilly Media. ISBN 9781491957660.
