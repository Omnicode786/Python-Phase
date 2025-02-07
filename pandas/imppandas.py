# .read_excel()	Reads data from an Excel file and creates a DataFrame.


import os
os.chdir(r"E:\Programming\Google  Python\Python-Phase\pandas")
import pandas as pd
dataframe_name = pd.read_excel("file_example_XLS_10.xls")
# describe()	Generates statistics summary of numeric columns in the DataFrame.
print(dataframe_name.describe())
