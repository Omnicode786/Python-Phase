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

# ‘r’	'r'	Read mode. Opens an existing file for reading. Raises an error if the file doesn't exist.
# ‘w’	'w'	Write mode. Creates a new file for writing. Overwrites the file if it already exists.
# ‘a’	'a'	Append mode. Opens a file for appending data. Creates the file if it doesn't exist.
# ‘x’	'x'	Exclusive creation mode. Creates a new file for writing but raises an error if the file already exists.
# ‘rb’	'rb'	Read binary mode. Opens an existing binary file for reading.
# ‘wb’	'wb'	Write binary mode. Creates a new binary file for writing.
# ‘ab’	'ab'	Append binary mode. Opens a binary file for appending data.
# ‘xb’	'xb'	Exclusive binary creation mode. Creates a new binary file for writing but raises an error if it already exists.
# ‘rt’	'rt'	Read text mode. Opens an existing text file for reading. (Default for text files)
# ‘wt’	'wt'	Write text mode. Creates a new text file for writing. (Default for text files)
# ‘at’	'at'	Append text mode. Opens a text file for appending data. (Default for text files)
# ‘xt’	'xt'	Exclusive text creation mode. Creates a new text file for writing but raises an error if it already exists.
# ‘r+’	'r+'	Read and write mode. Opens an existing file for both reading and writing.
# ‘w+’	'w+'	Write and read mode. Creates a new file for reading and writing. Overwrites the file if it already exists.
# ‘a+’	'a+'	Append and read mode. Opens a file for both appending and reading. Creates the file if it doesn't exist.
# ‘x+’	'x+'	Exclusive creation and read/write mode. Creates a new file for reading and writing but raises an error if it already exists.
