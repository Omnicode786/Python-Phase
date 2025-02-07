import pandas as pd
import numpy as np
import os

os.chdir(r"E:\Programming\Google  Python\Python-Phase\api")

URL="https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"

table = pd.read_html(URL)
df = table[3]
print(df)

df.columns = range(df.shape[1])
df = df[[0,2]]
df = df.iloc[1:11,:]
df.columns = ["Country","GDP M_USD"]

print(df)

df["GDP M_USD"] = df["GDP M_USD"].astype(int)
df["GDP M_USD"] = df["GDP M_USD"].round()
df["GDP M_USD"] = df["GDP M_USD"] / 1000
df["GDP M_USD"] = np.round(df["GDP M_USD"],2)

# df.rename(columns={"GDP M_USD" : "GDP B-USD"})
#  the issue in this is this doesnt create the instance like actually change it directly we need to reassign it still
#  a better way is simple
df.rename(columns={"GDP M_USD" : "GDP B-USD"}, inplace=True)
df["GDP T-USD"] = df["GDP B-USD"] / 1000
#  in the above way we can add a new colunm to the dataframe



print(df)
df.to_csv("world largest economies.csv", index=False)