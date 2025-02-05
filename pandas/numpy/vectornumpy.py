# NumPy is a Python library used for working with arrays, linear algebra, fourier transform, and matrices. NumPy stands for Numerical Python and it is an open source project. The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

import numpy as np


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

u = [1,2]
v = [3,4]
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
print(plt.plot(x,y))

