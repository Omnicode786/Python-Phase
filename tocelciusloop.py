#for loop in py can take 3 parameters as well

def tocel(x):
    return (x-32)*(5/9)

for x in range(0,101,10):
    #doing the above will not include 100 as we are stepping 10 each
    # so to counter this
    print(x, tocel(x))
#The range() function can take up to three parameters:  range(start, stop, step) 



#Stop - End of range

# value excluded from range (to include, use stop+1)

# no default

# must provide the ending index number 