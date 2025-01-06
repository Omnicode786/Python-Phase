with open("file io\\ben.txt") as file:
    for line in file:
        print(line.upper())


with open("file io\\ben.txt") as file:
    for line in file:
        print(line.strip().upper())
        # the strip function will strip away the new line 


file = open("file io\\ben.txt")
lines = file.readlines()
#readlines is diff from readline
file.close()
lines.sort()
print(lines)


# sorts the lines alphabetically and then print the lines 
# print is giving \n as new line
