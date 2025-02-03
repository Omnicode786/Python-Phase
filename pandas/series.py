import pandas as pd
# Create a Series from a list
data = [10, 20, 30, 40, 50]
s = pd.Series(data)
print(s)

# Accessing Elements in a Series


print(s[2])     # Access the element with label 2 (value 30)
print(s.iloc[3]) # Access the element at position 3 (value 40)
print(s[1:4])   # Access a range of elements by label


# values: Returns the Series data as a NumPy array.
# index: Returns the index (labels) of the Series.
# shape: Returns a tuple representing the dimensions of the Series.
# size: Returns the number of elements in the Series.
# mean(), sum(), min(), max(): Calculate summary statistics of the data.
# unique(), nunique(): Get unique values or the number of unique values.
# sort_values(), sort_index(): Sort the Series by values or index labels.
# isnull(), notnull(): Check for missing (NaN) or non-missing values.
# apply(): Apply a custom function to each element of the Series.

