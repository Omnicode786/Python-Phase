import pandas as pd
import os

os.chdir(r"E:\Programming\Google  Python\Python-Phase\pandas")

csv_path = "sets.csv"
df = pd.read_csv(csv_path)
print(df.head())
durationgreat100 = df[df["Duration"]>80]
print(durationgreat100)


#  write the new data to a new txt file

with open("newdata.txt", "w") as file:
    file.write(str(durationgreat100))
    durationgreat100 = df[(df["Duration"]>80) & (df["Pulse"] > 107)]
durationgreat100.to_csv("newcsv.csv", index=0, header=1)