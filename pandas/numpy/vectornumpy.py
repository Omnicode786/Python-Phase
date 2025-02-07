# NumPy is a Python library used for working with arrays, linear algebra, fourier transform, and matrices. NumPy stands for Numerical Python and it is an open source project. The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

import numpy as np



def Plotvec1(u, z, v):
    fig, ax = plt.subplots()  # Create a figure and axis
    
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)  # Red arrow for u
    plt.text(*(u + 0.1), 'u', color='r')  

    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)  # Blue arrow for v
    plt.text(*(v + 0.1), 'v', color='b')  

    ax.arrow(0, 0, *z, head_width=0.05, color='g', head_length=0.1)  # Green arrow for z
    plt.text(*(z + 0.1), 'z', color='g')  

    plt.ylim(-2, 2)
    plt.xlim(-2, 2)
    plt.grid()  # Optional: Add grid for better visualization

    plt.show()







print(np.__version__)

a = np.array([1,3,"Muzammil",88])

print(a)

print(type(a))
print(a.dtype)

print(a[0:3])

nums = np.array([1,2,3,4,5,6,7,8,9,10])

print(nums[1:11:2])
#  this  will print the even nums rem how slicing parameters works

### Numpy Statistical Functions

numbers = np.array([2,-1,22,10])
mean = numbers.mean()
print(mean)
# standard deviation
standard_daviation = numbers.std()
print(standard_daviation)
max = numbers.max()
min = numbers.min()

print(f"max: {max}, min: {min}")

# vectors

u = np.array([10,3])
v = np.array([4,11])
z = []

z = u+v
#  this will simply append the two
print(z)
#  this will correctly add the two vectors dimensionally
z = np.add(u,v)
print(z)

import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
plt.plot(x,y)
plt.show()
Plotvec1(u,v,z)
#  similarly we can also perform other vecotr operations


z = np.subtract(u,v)
print(z)
z = np.multiply(u,v)
print(z)
z = np.divide(u,v)
print(z)

#  dot product
z = np.dot(u,v)
print(z)

# x.y = x1y1 + x2y2

#  adding contant to a numpy array means it will be added to every element
u = u+1
print(u)



# 