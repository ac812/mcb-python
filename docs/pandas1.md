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

# Data manipulation with Pandas 

## What is Pandas?
No, it is not the plural of panda the bear!  Pandas is a Python package designed for data manipulation and analysis. Its name is derived from "**pan**el **da**ta" (not the bear!) and is also 
from "Python data analysis" [^McKinney]. It is especially popular for its data structures that help process tabular data 
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

Download the dataset from [here](https://drive.google.com/file/d/1CY6se8854BrQRx001779VwKlDcyu4vMM/view?usp=sharing) and save it into a `data` folder in your PyCharm project. 

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
Alternatively you can get the `dtype` of each column by using the `dtypes` attribute of the DataFrame; `df.dtypes`.  Note that
columns which hold string data values are imported into Pandas as `object` `dtype`.

To get the number of rows and columns that the DataFrame is made up of use the `shape` attribute:
```{code-cell} ipython3
df.shape
```
Note that `shape` is an attribute not a method, so not parentheses are used after `shape`.


## The Series

Each column in a DataFrame is a Series. A Series is a data structure in Pandas and is essentially a 1-dimensional array. 
{numref}`series` shows the main components of the Series. 

```{figure} images/series.png
---
name: series
---
Components of the Series data structure.
```

```{exercise-start} Exploring DataFrames
:label: exploring-df
```
**Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`

In this exercise we will be using the dataset from the World Bank Data Catalog that is used in this course.  Follow the 
instructions above to load the dataset into Python and make use of DataFrame methods or PyCharm to answer the following 
questions:

1. What type is `df`?
2. How many columns and how many rows does the `df` have?
3. What are the data types of each column?

```{exercise-end}
```



## Slicing DataFrames

{numref}`dataframe` shows the core components of the DataFrame data structure.  The first column we see when we look at the 
contents of `df` is the index.  The index is a column of data items in the DataFrame but rather it contains the index 
positions of each record in the DataFrame. Like all the other data structures in Python we have looked at so far, it 
starts with 0.  

```{figure} images/dataframe.png
---
name: dataframe
---
Components of the DataFrame data structure.
```

We can extract columns, rows or data items from DataFrames in different ways. The sections below go over the different ways 
we can slice DataFrames.

### Extracting column data (label-based indexing)
To extract data from a column in the DataFrame we use the following notation:  
**df["column_name"]**  
where `df` is the DataFrame object. If we want to extract multiple columns, we can provide a Python list of column names 
inside the square brackets as follows:  
**df[["column_name1", "column_name2"]]**

```{code-cell} ipython3
#extract the column "life_expectancy_t" and save it in variable le_t
le_t = df["life_expectancy_t"]

#check what type is le_t
print(f"Type of le_t is: {type(le_t)}")

# get the length of the Series
print(f"Size of le_t is: {le_t.size}")

#print the first 5 items
le_t.head()
```

Note that in the example above, since we are extracting only one column from `df` the result of the first slicing is a Series object. 
In the code below, on the other hand, extracts 3 columns from `df`, and therefore the result of this is another DataFrame object.

```{code-cell} ipython3
#extract the columns "life_expectancy_t", "life_expectancy_m", "life_expectancy_f" and save it in variable le
le = df[["life_expectancy_t", "life_expectancy_m", "life_expectancy_f"]]

# get type of object returned from slicing
print(f"Type of le is: {type(le)}")

#get size of DataFrame
print(f"Size of le is: {le.shape}")

# print the first 5 items
le.head()
```


### Extracting row data (boolean indexing)
We can extract rows from our DataFrame that meet a specified condition by using the conditional expressions in our slice operators as follows:  
**df[conditional expression]** 

Let us try an example on our `df` DataFrame.  We would like to get the records where life expectancy is more than 80:

```{code-cell} ipython3
:tags: [output_scroll]

le_top = df[df["life_expectancy_t"] > 80]
le_top.head()
```

Similarly to Numpy, you can combine different comparison expressions using the `&` (and) or `|` (or) operators.  You would 
need to wrap each conditional expression in parentheses.  See example below:

```{code-cell} ipython3
:tags: [output_scroll]
# get all records that have life expectancy > 80, where year is either 2020 or 2019
le_top[(le_top["year"] == 2020) | (le_top["year"] == 2019)]
```

You can write the same code using the `isin()` function which providing it with a list of values, it returns `True` for 
each row where the values are present.  The example below returns the same result as the code above, but it uses the `isin()` 
function to check whether each row in `le_top` has either `2000` or `2019` in the `year` column.

```{code-cell} ipython3
:tags: [output_scroll]

le_top[le_top["year"].isin([2020, 2019])]
```

### Extracting rows and columns

To extract rows and columns from a DataFrame we need to use the `loc` and `iloc` operators in front of the square brackets.

#### `loc`

`loc` is mainly used with label-based indexing and boolean indexing. The general usage format is the following:  
**df.loc[row condition expression, column_name]**  
In the example below we extract the list of countries from our `df` DataFrame where life expectancy is greater than 80. 

```{code-cell} ipython3
countries = df.loc[df["life_expectancy_t"] > 80, "country"]

print(f"Type of countries is: {type(countries)}")
print(f"Length of Series is: {countries.size}")

# use unique method of Series to remove duplicates
print(countries.unique())
```

#### `iloc` (integer-based indexing)
`iloc` is mainly used with integer-based indexing, which means that index positions are supplied to `iloc` in the following 
format:  
**df[R, C]**  
where *R* is the row index position and *C* is the column index position. In short, if you want to extract data items from a 
DataFrame based on index positions, than `iloc` is the way to do that.

```{code-cell} ipython3
#get the first 10 rows and the first 5 columns of the df Dataframe
df.iloc[0:10, 0:5]
```

```{exercise-start} Slicing DataFrames
:label: slicing-df
```
**Level:** {octicon}`star-fill;1em;sd-text-warning` {octicon}`star-fill;1em;sd-text-warning` {octicon}`star;1em;sd-text-warning`

Using the `df` DataFrame created above, write code to perform the following tasks: 
1. Get the first 3 columns of `df`.
2. Get the first 3 rows of `df`.
3. Get the first row of `df`.
4. What are the maximum and minimum values of life expectancy (use *life_expectancy_t* column)?  Which countries have these?
5. Extract all the data from the United Kingdom and save it into another DataFrame.  How many records were returned?
6. Extract all the records from the United Kingdom from the year 2020.  How many records were returned? 
7. When extracting rows from a DataFrame, try not using parentheses between two conditional expressions when using `&` or `|` and see what happens.
```{exercise-end}
```





[^world-bank]: The World Bank: World Development Indicators Collection.  Terms of Use [here](https://www.worldbank.org/en/about/legal/terms-of-use-for-datasets).  This dataset can also be viewed interactively on the World Data Bank website [here](https://databank.worldbank.org/Teaching-Python-dataset/id/48401a76).  
[^McKinney]: McKinney, Wes (2017). *Python for Data Analysis, Second Edition*.  O'Reilly Media. ISBN 9781491957660.
