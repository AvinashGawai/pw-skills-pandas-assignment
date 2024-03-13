import pandas as pd
# Q1. Create a Pandas Series that contains the following data: 4, 8, 15, 16, 23, and 42. Then, print the series.

l1 = [4, 8, 15, 16, 23, 42]
df = pd.Series(l1)
print(df)
print(type(df))
# Q2. Create a variable of list type containing 10 elements in it, and apply pandas.Series function on the
# variable print it.

l2 = [i for i in range(1, 11)]
df1 = pd.Series(l2, index=l2)
print(df1)
print(type(df1))
# Q3. Create a Pandas DataFrame that contains the following data:
table = {'Name': ['Alice', 'Bob', 'Claire'],
         'Age': [25, 30, 27],
         'Gender': ['Female', 'Male', 'Female']}
index1 = [i for i in range(1, 4)]
df2 = pd.DataFrame(table, index=index1)
print(df2)
# Q4. What is ‘DataFrame’ in pandas and how is it different from pandas.series? Explain with an example.

'''a DataFrame is a two-dimensional labeled data structure capable of holding data of different types. It is similar 
to a spreadsheet or SQL table, where data is organized into rows and columns. Each column in a DataFrame is a pandas 
Series. A pandas Series, on the other hand, is a one-dimensional labeled array capable of holding data of any type. 
It can be thought of as a single column of data.'''

import pandas as pd

# Creating a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

df = pd.DataFrame(data)
print("DataFrame:")
print(df)

# Creating a Series
ages = pd.Series([25, 30, 35, 40], name='Age')
print("\nSeries:")
print(ages)
# Q5. What are some common functions you can use to manipulate data in a Pandas DataFrame? Can
# you give an example of when you might use one of these functions?

# head() and tail(): These functions allow you to view the first or last few rows of a DataFrame, respectively. They
# are useful for quickly inspecting the structure of your data.
df.head()  # View the first 5 rows of the DataFrame

# describe(): This function generates descriptive statistics summarizing the central tendency, dispersion, and shape
# of the distribution of a DataFrame's numeric columns.
df.describe()  # Generate summary statistics of the DataFrame

# info(): This function provides a concise summary of a DataFrame, including the data types, non-null values,
# and memory usage.
df.info()  # Display a concise summary of the DataFrame

# dropna(): This function removes missing values (NaN) from a DataFrame.
df.dropna()  # Remove rows with missing values

# fillna(): This function fills missing values in a DataFrame with specified values.
df.fillna(0)  # Fill missing values with 0

# Q6. Which of the following is mutable in nature Series, DataFrame, Panel?

# Among the options provided, Series and DataFrame are mutable in nature, while Panel is not.
#
# Series: Individual elements in a Series can be modified after creation.
# DataFrame: Columns and rows in a DataFrame can be modified after creation.
# However, Panel objects have been deprecated since version 0.25.0 and are no longer recommended
# for general use. They were mutable, allowing changes to the data they contained, but due to their
# limited use and inefficiency compared to other data structures, they were removed from the main
# pandas library. Instead, for three-dimensional data, you can use the MultiIndex DataFrame.

# Q7. Create a DataFrame using multiple Series. Explain with an example.
df4 = pd.DataFrame(df, df1)
print(df4)

# To create a DataFrame using multiple Series, you can combine these Series into a dictionary and
# then pass that dictionary to the pd.DataFrame() constructor. Each Series will represent a column
# in the resulting DataFrame.

# Creating multiple Series
names = pd.Series(['Alice', 'Bob', 'Charlie', 'David'])
ages = pd.Series([25, 30, 35, 40])
cities = pd.Series(['New York', 'Los Angeles', 'Chicago', 'Houston'])

# Combining Series into a dictionary
data = {'Name': names, 'Age': ages, 'City': cities}

# Creating DataFrame using the dictionary
df = pd.DataFrame(data)

print(df)
