# Array Creation: Numpy arrays are similar to Python lists but are fixed in size and contain elements of the same type.
# Basic Operations: Numpy allows for efficient operations like indexing, slicing, and mathematical operations (e.g., vector addition, subtraction, and multiplication).
# Attributes: Important attributes include size (number of elements), ndim (number of dimensions), and dtype (data type of elements).
# Universal Functions: Numpy supports operations on arrays, such as calculating the mean or maximum values.
# Broadcasting: This feature allows operations to be performed on arrays of different shapes.


#  its type is numpy.ndarray

import numpy as np

a = np.array([1,22,22,34,55])
print(a)
type(a)
# lenght o f the array
print(a.size)

# dimensions of the array
print(a.ndim)

# gives size of array in each dimension it is in tupple
print(a.shape)

#  we can slice np arrays as well

b = a[1:4]
print(b)