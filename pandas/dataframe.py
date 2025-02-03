import pandas as pd
import os

os.chdir(r"E:\Programming\Google  Python\Python-Phase\pandas")



csv_path = "email.csv"
# here df is short for dataframe
df = pd.read_csv(csv_path)
print(df.head())
Emails = df[["Login email"]]
print(Emails)
#  similarly we can read excel sheets files as well

#  they work best with , and not ; the email file you provided had ; first so rem the output was in a bad pattern


#  data frame is compired of rows and columns

#  we can create dataframe out of dictionary as well

friends = {"BestFriends":["Taha","Ahsan", "Suman"],
            "Good Friends": ["Minhaj", "Mustufa", ""],
            "Ratings": ["10", "5", "77"]
        }
#  all lists must be of same length as its basically a list they are comprised of that

#  keys coresponds to the colunms and the lists in the value perform as rows


dataframeoffriends = pd.DataFrame(friends)
# dataframe is added to make the file a dataframe

print(dataframeoffriends)
with open("Emails.txt", "w") as file:
    for email in Emails["Login email"]:
        file.write(email + '\n')

# this only  gives one colunm of the dataset
Bestfriends = dataframeoffriends[["BestFriends"]]
#  similar to this we can extract more htan one colunms as well
 
AllFriends = dataframeoffriends[["BestFriends", "Good Friends"]]

print(Bestfriends)
print(AllFriends)

#  using singel breackets give us a series and double brackets gives a dataframe
#  this is meta data A Series is like a single column of data, while a DataFrame is a table with multiple columns. Let’s break it down.
# A Series is a one-dimensional array that holds a single column of data.


#  we can also do indexing to access colunms and rows
print(dataframeoffriends.iloc[0][0])
#  we can also do it like this

print(dataframeoffriends.loc[1,"BestFriends"])

# A DataFrame is a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns).

#  we can also find uniqeness of a dataframe

df1 = df[df["Year"]>2017]
#  in this way we can get only the certain data which are of 2017 year and above similarly we can do alot
print(df1)