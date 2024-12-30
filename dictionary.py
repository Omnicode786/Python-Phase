filecoutns = {"jpg": 10, "txt": 2, "py":24}

print(filecoutns)
print(filecoutns["txt"])
print("jpg" in filecoutns)
print("jdspg" in filecoutns)
#dictionarty are mutable we can add

filecoutns["csv"] = 8
print(filecoutns)

#if we try to add a key that already present it updates the value / replaced
filecoutns["txt"] = 12
print(filecoutns)

#if we want to delete then
del filecoutns["py"]
print(filecoutns)

# if we use a for loop in dict then it will iterate throught hte keys in the dictionary

for extensions in filecoutns:
    print(extensions, end= " ")

#one method to access the keys is the items method
print()
for extension, amount in filecoutns.items():
    print(f"There are {amount} in the .{extension} extension")

#if we want seperate then

for value in filecoutns.values():
    print(value,end=" ")
print()
for key in filecoutns.keys():
    print(key, end=" ")
print()
