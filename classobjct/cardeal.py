# You are working on a Python program to simulate a car dealership's inventory management system. The system aims to model cars and their attributes accurately.



class Car(object):
    def __init__(self, maxspeed, mileage, color):
        self.maxspeed = maxspeed
        self.mileage = mileage
        self.color = color
    def seat_capacity(self, capacity):
        self.capacity = capacity
    def display_prop(self):
        print("The properties fo the car are")
        print(f"The color of the car is {self.color}")
        print(f"The maxspeed of the car is {self.maxspeed}")
        print(f"The mileage of the car is {self.mileage}")
        print(f"The capacity of the car is {self.capacity}")


print()

car1 = Car(20,50, "white")
car1.seat_capacity(8)
car1.display_prop()
print()
car1 = Car(90,100, "red")
car1.seat_capacity(4)
car1.display_prop()
print()
car1 = Car(220,120, "black")
car1.seat_capacity(1)
car1.display_prop()

x = 1 
x = x > 5
print(x)