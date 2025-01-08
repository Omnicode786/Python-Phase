import csv

f= open("csv\\csvtexts.txt")
csvfile = csv.reader(f)
next(csvfile)
# this will skip the first line now techinically this will skip as many lines as you want anywhere
for row in csvfile:
    name,phone,role = row
    print(f"{name} number is {phone} and role is {role}")

    # just seperate them by , no need to use th next line

