import os

def checker(directory):
    allfiles = os.listdir(directory)
    # now all all files is a list whihc contains all the files and the other directories in the paremeter of the directory
    for name in allfiles:
        fullname = os.path.join(directory, name)
        # this will simply give the absolute path of the file rem 
        if os.path.isdir(fullname):
            print(f"This file {name} is a directory located at {fullname}")
        else:
            print(f"The given file {name} is a file which is located at {fullname}")


checker(r"E:\Programming\Web-dev\Web-Development")