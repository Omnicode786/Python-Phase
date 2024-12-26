def loop():
    string = "A"
    for i in range(26):
        print(string)
        # str+=1
        # in python we cannot  directly doo ++ to a string
        # this plus plus simply means that we are trying to concatenate something to the orignal string so that will not work
        #instead we use the ord function to get the ascii value of the code and then convert it to string 
        # string = str(ord(string) + 1)
        #this will also not work as thsi would give us directly 65
        string = chr(ord(string)+1)
loop()

def triangle():
    for i in range(1,5):
        string1 = "A"
        for j in range(i):
            print(string1, end=" ")
            string1 = chr(ord(string1)+1)
        print() #this will create a nbew line 
     #print function adds the new line in order to tacke that we add end = " " after ,
triangle()