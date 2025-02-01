# try except else finally 
import os
os.chdir("E:\Programming\Google  Python\Python-Phase\exception handeling")

with open ("filename.txt", "w") as file:
    file.write("Hello")



try:
    getfile = open("filename.txt", "a")
    getfile.write("Try except else and finally")
except IOError:
    print("Unable to detect")
else:
    print("The file was written succesfully")
finally:
    getfile.close()
    print("File is now closed")

a = 1
try:
    b = int(input("Please enter a number to divide a: "))
    a = a / b
    print("Success a =", a)
except:
    print("There was an error")
