
import os
os.chdir(r"E:\Programming\Google  Python\Python-Phase\file io")

with open("file.txt", "r") as file1:
    with open("file1.txt", "a") as file2:
        for line in file1:
            file2.write(line)
            file2.tell()

# .tell() - returns the current position in bytes
# .seek(offset,from) - changes the position by 'offset' bytes with respect to 'from'. From can take the value of 0,1,2 corresponding to beginning, relative to current position and end