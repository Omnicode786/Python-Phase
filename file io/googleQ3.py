
# The file_date function creates a new file in the current working directory, checks the date that the file was modified, and returns just the date portion of the timestamp in the format of yyyy-mm-dd. Fill in the gaps to create a file called "newfile.txt" and check the date that it was modified

import os
import datetime

def file_date(filename):
  # Create the file in the current directory
  with open("newfile.txt", "w") as file:
    pass
  timestamp = os.path.getmtime("newfile.txt")
  # Convert the timestamp into a readable format, then into a string
  datetill = str(datetime.datetime.fromtimestamp(timestamp))
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{}".format(datetill[0:10]))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd