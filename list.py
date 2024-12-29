sentence = "My name is muzammil Alam"

def getingword(sentence, n):
    word = sentence.split()
    # the split function basically splits the string into words and returns a list of words
    # in python strings and lists are similar in some ways and are in sequence
    # once you know it for one data type you can use it for the other the indexing technique is the same
    if n > len(word):
        return "Index out of range"
    return word[n-1]

print(getingword(sentence, 4))
print(getingword(sentence, 2))



fruits = ["Mango","Kiwi", "Peaches","Kiwi"]
print(fruits)

fruits.insert(0,"Pinapple")
print(fruits)

# this basically makes the list longer and adds the element at the given index and shifts the rest of the elements to the right
fruits.insert(24,"Banana")
# if we add an index that is greater than the length of the list it would add the element at the end of the list
print(fruits)

fruits.remove("Kiwi")
#this would remove only the first occurence of the element in the list
print(fruits)
# agar koi element list me nahi hota toh error aata hai
# agar element list me hota hai toh wo remove hojata hai
#aik or tareeqa hai remove ka pop method
print(fruits.pop(2))
# this would remove the element at the given index and return the element that is removed
print(fruits)
# aik or direct method he remove ya change krne ka
fruits[1] = "Orange"
print(fruits)
# hey ai give me example of the list used above in the code
# // this is an example of list in python