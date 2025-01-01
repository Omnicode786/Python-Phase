# When writing a Python class, you define a method called __init__ to be your constructor. The special name tells Python to use that method as the constructor. Just like any other method, the constructor can take arguments. When making an argument to the class, the first constructor must always be self.




class Apple:
    def __init__(self):
        self.color = "red"
        self.flavor = "sweet"

honeycrisp = Apple()
print(honeycrisp.flavor)
print(honeycrisp.color)


# prints "red"


class cat:
    def speak(self, name = "Meow Meow"):
        print(f"The cat says {name}")

# this way when we dont give any argument the cat still says meow meow now as of now I know nothing about self innit etx
simba = cat()
simba.speak()