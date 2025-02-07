# Key aspects of NumPy in Python:
# Efficient data structures: NumPy introduces efficient array structures, which are faster and more memory-efficient than Python lists. This is crucial for handling large data sets.

# Multi-dimensional arrays: NumPy allows you to work with multi-dimensional arrays, enabling the representation of matrices and tensors. This is particularly useful in scientific computing.

# Element-wise operations: NumPy simplifies element-wise mathematical operations on arrays, making it easy to perform calculations on entire data sets in one go.

# Random number generation: It provides a wide range of functions for generating random numbers and random data, which is useful for simulations and statistical analysis.

# Integration with other libraries: NumPy seamlessly integrates with other data science libraries like SciPy, Pandas, and Matplotlib, enhancing its utility in various domains.

# Performance optimization: NumPy functions are implemented in low-level languages like C and Fortran, which significantly boosts their performance. It's a go-to choice when speed is essential.



# You can create NumPy arrays from Python lists. These arrays can be one-dimensional or multi-dimensional

# Element-Wise Functions	Applying functions to each element.
import numpy as np
arr = np.array([[1,9,4],[36,49,64]])
result = np.sqrt(arr)
print(result.astype(int))
#  this eliminates the decimal points also w could use round or floor


import os
os.chdir(r"E:\Programming\Google  Python\Python-Phase\pandas\numpy")
with open("Example1.txt","r") as file1: 

     FileContent=file1.read() 


print(FileContent)