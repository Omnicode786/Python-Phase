def greetings(name, department):
    print("Hello",name,"from",department)

# // this does not return any value 
greetings("Muzammil", "Software Engineering")
greetings("M-Suman", "Software Engineering")


def convertsec(seconds):
    hours = seconds // 3600
    minutes = (seconds -hours*3600) // 60
    second = seconds - hours*3600 - minutes*60
    print(hours,minutes,second)
    return hours, minutes, second
    # two // simply means this is an integer division meaingn it would be truncated how it is in int division
convertsec(int(input('Enter ampount in seconds: ')))
# rem that input function returns the value in string so we need to covert it into int
hours,minutes,seconds =  convertsec(int(input('Enter ampount in seconds: ')))

print(hours,minutes,seconds)
# // this is an example of returning function that returns a value 

#  now let's do a void function taht doesnt retunrn any vcalue
result = greetings("Umer shafqat", "Buisness")

print(result)
# // this woould print none as none measn empty in python it is a type of data type 



