# The create_python_script function creates a new python script in the current working directory, adds the line of comments to it declared  by the 'comments' variable, and returns the size of the new file. Fill in the gaps to create a script called "program.py".

import os
def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename, "w") as pythonfile:
    pythonfile.write(comments)
    # rem to pass the filname as the argument in the getsize and other such functionas it expcts astring and not the
    filesize = os.path.getsize(filename)
  return(filesize)

print(create_python_script("program.py"))
