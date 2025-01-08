import csv

file = open("csv\\csvtexts.txt")
csvfile = csv.DictReader(file)

for row in csvfile:
    name = row.get("Name")
    phone = row.get("Phone")
    role = row.get("Role")
    print(f"{name} number is {phone} and role is {role}")

    #this is a much better approach then the previous one