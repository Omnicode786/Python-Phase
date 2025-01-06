# this is input output stuffs

file = open(r"file io\ben.txt")


# print(file.readline())
# print(file.readline())
# this would give one line at a time and because of that print function would give a new line


print(file.read())
file.close()


#when a file is open in a your code so it is not able to run on other things like you know the delete things

# they create race conditions

with open("file io\\new.txt") as files:
    print(files.readline())
    #with block automatically closes the file


