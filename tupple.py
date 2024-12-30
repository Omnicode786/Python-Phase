
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
#  there is also a tupple operator which coverts any thing into a tupple

name = ["Muhammad","Muzammil","Alam"]
print(name)
tupplename = tuple(name)

print(tupplename)

#  although tupples themselves cannot be changed but the data inside an element of the tupple can be here is the example

mytupple = ('77', 665,"Muzammil", [3,66,88.88])
print(mytupple)

'''
if we were to directly change it to like mytupple[0] = 3 then this would give error but
'''
mytupple[3][2] = 99.12
print(mytupple)
# get it meri jan ke tote

# function to explain this can be

def tuppleexplainer(a,b):
    if(b!=0):
        dividor = a /b
    else:
        dividor = "Eror in dividing by 0"
    
    return a+b, a-b, a*b, dividor

add,subtract,multiply,divide = tuppleexplainer(55,5)
print(add,subtract,multiply,divide)

add,subtract,multiply,divide = tuppleexplainer(1,6)
print(add,subtract,multiply,divide)

add,subtract,multiply,divide = tuppleexplainer(55,0)
print(add,subtract,multiply,divide)

string = "Muzammil"
print(string[-3:])
string.replace([string.index[-1]],"h")
print(string)