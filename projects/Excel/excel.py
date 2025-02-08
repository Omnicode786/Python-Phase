from openpyxl import Workbook
from win32com.client import Dispatch
import os
import pandas as pd
from openpyxl.utils.dataframe import dataframe_to_rows
from faker import Faker
import numpy as np

os.chdir(r"E:\Programming\Google  Python\Python-Phase\projects\Excel")

fake = Faker()
num_employees = 10

data = {
    "Employee ID": range(1001, 1001 + num_employees),
    "Name": [fake.name() for _ in range(num_employees)]
    
    # the _ is simply the index which we dont want so we use this syntax


    # names = []
    # for _ in range(num_employees):
    # names.append(fake.name()) 
    # essentially the above is happening under the hood of the cryptic syntax
    ,
    "Department": np.random.choice(["IT", "HR", "Finance", "Marketing", "Operations", "Sales", "R&D"], num_employees),
    "Salary": np.random.randint(40000, 200000, num_employees),
    "Joining Date": [fake.date_between(start_date="-15y", end_date="today") for _ in range(num_employees)],
    "Experience (Years)": np.random.randint(1, 40, num_employees),
    "Performance Rating": np.round(np.random.uniform(2.5, 5.0, num_employees), 1),
    "Age": np.random.randint(22, 65, num_employees),
    "Location": [fake.city() for _ in range(num_employees)],
    "Email": [fake.email() for _ in range(num_employees)],
}

df = pd.DataFrame(data)


workbook = Workbook()
sheet = workbook.active

#  now lets use pandas data frame


# sheet['A1'] = "Name"
# sheet['B1'] = "Age"


# instead of doing this or anything above
#  and below

# for row in dataframe_to_rows(df, index=False, header=True):
#     sheet.append(row)


# workbook.save(filename="try_excel.xlsx")

#  now to open the excel sheet directly from here


#  just do this

df.to_excel("try_excel.xlsx", index=False)

xl = Dispatch("Excel.Application")
xl.visible = True

workbook1 = xl.Workbooks.Open(r"E:\Programming\Google  Python\Python-Phase\projects\Excel\try_excel.xlsx")
