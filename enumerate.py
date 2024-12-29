#enumarate is like a function that returns a tuple with the index and the value of the element

winner= ["Muzammil", "Suman", "Taha"]

for index , person in enumerate(winner):
    print(index+1, person)

strings = ["a", "b", "c", "d", "e"]
strings1 = ["pineapple", "apple", "banana", "kiwi", "orange"]

def lister(strings):
    result = []

    for index, character in enumerate(strings):
        if index % 2 == 0:
           result.append(character)    
    # idhr ham ne ek empty list banai he or usme elements add krne ke liye ek loop chalaya he or basically bar bar empty kr rhe hen tbhi function ke andr dala hai
    #or append function se elements add kr rhe hen jisse aik ke bad aik elements add hote jate hen smjhe bhulakar
    #meri jan ke tote
    return result
print(lister(strings))
print(lister(strings1))
# this only prints the elements at the even index also meri jan ke tote enumerate to kch bhi ni he smjho yeto simply tupple ke upr index or uske andr ki value deta hai
