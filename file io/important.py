import os

# Correct the file path
os.chdir(r"E:\Programming\Google  Python\Python-Phase\file io")

# Writing multiple lines to the file
with open("file.txt", "w") as file:
    file.write("This is a sample line.\n")
    file.write("This line is important.\n")
    file.write("Another regular line.\n")
    file.write("Something important is here too.\n")

# Reading and finding important lines
with open("file.txt", "r") as file:
    for line_number, line in enumerate(file, start=1):  # Track line number
        if "important" in line:
            print(f"Line {line_number}: {line.strip()}")