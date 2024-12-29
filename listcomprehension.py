multiples = []

for x  in range (1,11):
    multiples.append(x*7)
print(multiples)


# in python doing the above is quiete common so python has a way to do this in a single line
# this is called list comprehension

multiples = [x* 7 for x in range(1,11)]
print(multiples)
# this works for any other sequence as well

# for strings it may be as

languages = ["python", "java", "c++", "c#"]
lengths = [len(language) for language in languages]
print(lengths)
# for numbers we could possibly right it as
numbers = [x for x in range(1,101) if x % 3 == 0]
print(numbers)