log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
index = log.index("[")
print(log[index+1:index+6])

import re
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])


# This regular expression matches a string enclosed in square brackets followed by one or more digits. Then, it uses the re.search() function to search the string log for a match to the regular expression. The re.search() function returns a Match object if a match is found, or None if no match is found. the re.search() function returns a Match object because the string log contains a match to the regular expression. The Match object has a group() method that returns the captured groups from the match. In this case, the only captured group is the number, which is returned by the result[1] expression.




# this is . is a wild card in regex
#  adds like a indicator of some color
# a dot . mathces any character it can be replaced by any character in the reserve dthing
#  to look fo r a string that starts with the string let's suppose fruit we wil use
# ^fruir

# try to  always use raw strings in regex python so it sends the string as is without interpretiing any special characters

result1 = re.search(r"aza", "plaza")
print(result1)
# <re.Match object; span=(2, 5), match='aza'>  2 is starting index and 5 is not included so index- 1
print(re.search(r"p.ng", "penguin"))
print(re.search(r"^peng", "penguin"))

def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True

# to make it case insensitive
print(re.search(r"p.ng", "Penguin"))
#  this will make it none as P is capital
print(re.search(r"p.ng", "Penguin", re.IGNORECASE))
#  now ill print
#  this sort of can also be done with this method 
print(re.search(r"[Pp].ng", "Penguin"))
#  this is medioclrly strict

print(re.search(r"[a-z]ng", "penguin"))
print(re.search(r"[a-z][a-z]ng", "penguin"))
#  this guives any thing at firtst and then the follow along
#  not e that this will not work on if there is a space thingi
def check_punctuation (text):
  result = re.search(r"[.?!,:;]", text)
  return result != None
  

print(re.search(r"cats|dogs", "I like dogs"))
#  basically works like or gate
print(re.search(r"cats|dogs", "I like cats and dogs both"))
#  we only get the 1st one
#  in order to fina all
print(re.findall(r"cats|dogs", "I like cats and dogs both"))
# return a list of all the matches
print(re.search(r"pe.*n", "penguin"))
#  this means match pe multipied buy any other thing coming accross it
print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False
def returner():
  return 0

returner()