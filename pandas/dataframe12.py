# DataFrames provide numerous attributes and methods for data manipulation and analysis, including:

# shape: Returns the dimensions (number of rows and columns) of the DataFrame.
# info(): Provides a summary of the DataFrame, including data types and non-null counts.
# describe(): Generates summary statistics for numerical columns.
# head(), tail(): Displays the first or last n rows of the DataFrame.
# mean(), sum(), min(), max(): Calculate summary statistics for columns.
# sort_values(): Sort the DataFrame by one or more columns.
# groupby(): Group data based on specific columns for aggregation.
# fillna(), drop(), rename(): Handle missing values, drop columns, or rename columns.
# apply(): Apply a function to each element, row, or column of the DataFrame.


import pandas as pd
# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
print(df)
print(df['Name'])  # Access the 'Name' column
print(df.iloc[2])   # Access the third row by position
print(df.loc[1])
print(df[['Name', 'Age']])  # Select specific columns
print(df[1:3]) 
print()
print()

unique_dates = df['Age'].unique()
print()
print()
print(unique_dates)


high_above_102 = df[df['Age'] > 25]
high_above_102 = df[df['Age'] > 25]

import os
os.chdir(r"E:\Programming\Google  Python\Python-Phase\pandas")
df.to_csv('trading_data.csv', index=False)
