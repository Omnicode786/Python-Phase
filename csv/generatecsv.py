import csv
import os
nowpath = os.getcwd()
directory = os.path.join(nowpath, "csv")
os.chdir(directory)
hosts = [["lanline", "192,168.0.1"], ["Ethernet", "5500"]]
with open("host.csv", "w" , newline="") as hostcsv:
    writer = csv.writer(hostcsv)
    writer.writerows(hosts)

