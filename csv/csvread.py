
import csv
file = open("csv\\host.csv")
content = csv.reader(file)
for row in content:
    host, ip = row
    print(host, ip)