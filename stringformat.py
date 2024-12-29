name = "Muzammil"
department = "Electronics"

print("From {} department welcome {}".format(department, name))
# they can be interchanged
percentage = 88.927
print("{} you got {:.2f}% in your exams".format(name, percentage))
# the :.2f will format the code in floating point number into two decimal places
#This method automatically handles any conversion between data types for us. 
# the expression {:>3.2f} would align the text three spaces to the right, as well as specify a float number with two decimal places


print(len("abcde"))
for c in "abcde": print(c)
print("abc" in "abcde")  # prints True
print("def" in "abcde") 
print("abcde"[2])  # prints "c"
print("abcde"[-1])
print("abcde"[0:2])   # prints "ab"
print("abcde"[2:])
print("AaBbCcDdEe".lower()) 
print("AaBbCcDdEe".upper())
print("   Hello   ".lstrip()) 
print("   Hello   ".rstrip())
print("   Hello   ".strip())
print("12345".isnumeric())# prints True
print("-123.45".isnumeric()) 
print("xyzzy".isalpha())
test = "How-much-wood-would-a-woodchuck-chuck"
print(test.split("-"))
print(test.split())
print(test.replace("wood", "plastic"))
print("-".join(test.split()))


