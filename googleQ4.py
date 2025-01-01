# Concatenate a value, a string, and the key for each item in the dictionary and append to the end of a new list[ ] using the list.append(x) method.  

# Iterate over keys with multiple values from a dictionary using nested for loops with the dictionary.items() method.


def fullnamefunc(empnames):
    fullnames = []
    for lastname, firstname in empnames.items():
        fullnames.append(firstname + " " + lastname)
    return " ".join(fullnames)

empnames = {
    "Alam": "Muzammil", "Suman":"Muhammad", "Ahmed":"Ali"
}
print(fullnamefunc(empnames))