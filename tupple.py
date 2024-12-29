
# the tupples are immutable becuase lets say we have a list [firstname, middlename, lastname] here if we were to add another set of data then 
#that would not make sense and hence we use tupples where we can have a fixed set of data

def tuppleexplain(firstname, middlename, lastname):
    tupple = (firstname, middlename, lastname)
    # similar to here the position of the elements inside the it have a meaning
    return firstname, middlename, lastname
tuppleexplain("Muhammad", "Muzammil", "Alam")
print(type(tuppleexplain("Muhammad", "Muzammil", "Alam")))
# the order matters in the tupples
#when a function returns more than one value its basically returns a tupple
# we can unpack the tupple by assigning the values to the variables 
# like this
firstname, middlename, lastname = tuppleexplain("Muhammad", "Muzammil", "Alam")
print(firstname, middlename, lastname)
# toring the elements of a tuple in separate variables is called unpacking.