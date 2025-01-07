import os

# os.remove("file io\\write.txt")
# simply delete the following file

# simply renames the file

exist = os.path.exists("file io\\replacednew.txt")
if exist:
    os.rename("file io\\replacednew.txt", "file io\\replacednew2.txt")

print(exist)

#check if it exists or not

#check how a big a size of the file is
size = os.path.getsize(r"c:\Users\lkj\OneDrive\Desktop\Rush.Hour.3.(2007).720p.Dual.Audio.(Hin.Eng).[MoviesFlix.NeT].man")
print(size)

size = size / 1024**2
print(f"{size:.2f}MB")

# how to check when was the file last modified
# the result is in time stamp no of secs since jan 1st 1970
#it is unix timestamp

print(os.path.getmtime("file io\\replacednew2.txt"))
import datetime
#to counter the above
timestamp = os.path.getmtime("file io\\replacednew2.txt")
print(datetime.datetime.fromtimestamp(timestamp))

file= "file io\\replacednew2.txt"
if os.path.isfile(file):
    print(os.path.isfile(file))
    #the is file function basically tells if the given path is a file or not where as it 
    # in if exists this one basically tells whether the path exists or not regardless of the fact it is a file or not

    print(os.path.getsize(file),"Bytes")
else:
	print(os.path.isfile(file))
	print("File not found")



# os.path.abspath this will give us the absolute of the relativ path entered
# os.getcwd() this will give us our working directory

# to create a directory we use os.mkdir("nameofdirectory")
# os.chdir("the directory we want to go") this will take our cwd to the entered directory


#in order to delete a directory we first need to delete all the files in it
# os.rmdir()
# os.listdir(directory) this wil give us all the items in the directory included files and direcrories 


