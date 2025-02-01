import matplotlib.pyplot as plt

class Circle(object):
    def __init__(self, color, radius):
        self.radius = radius
        self.color = color
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show() 
    # method
    def addradius(self, r):
        self.radius = self.radius + r
class Rectangle:
    # this init is basically a constructor
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), height=self.height,width=self.width , fc=self.color))
        plt.axis('scaled')
        plt.show() 




RedCirlce = Circle("red", 10)


print(RedCirlce)
print(RedCirlce.color)
print(RedCirlce.radius)
RedCirlce.radius = 55
print(RedCirlce.radius)
RedCirlce.addradius(12)
print(RedCirlce.radius)
RedCirlce.drawCircle()


YellowRectangele = Rectangle(10,18, "yellow")
YellowRectangele.drawRectangle()