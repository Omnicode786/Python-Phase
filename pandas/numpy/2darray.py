import numpy as np

nums = [[11,12,13],[133,12,32],[33,44,55]]
nums1 = [[1,2,3],[4,5,6],[7,8,9]]
A = np.array(nums)
B = np.array(nums1)
print(A.size)
print(type(A))
print(A.ndim)
print(A.shape)

# NumPy arrays support advanced indexing, which allows a more compact syntax:

print(A[0:2,2])
#  the above is equivalent to
# print(nums[0:2][2])
# However, when you chain indexing (like A[0:2][2]), it first creates a new temporary array from A[0:2]. Since this temporary array has fewer rows, indexing beyond its limits results in an IndexError.

# in normal lists to achieve something like this we will  have to use a loop that is why numpy is powerful

third_colunm = []
for row in nums:
    #  we can also do slicing on the nums list here above
    third_colunm.append(row[2])
    print(third_colunm)
#  in this we can use access the list indesxing

C = A+B
print(C)
#  a better way would be
C = np.add(A,B)
print(C)
C = np.dot(A,B)
print()
print(C)

A = np.array([[0, 1, 1], [1, 0, 1]])
B = np.array([[1, 1], [1, 1], [-1, 1]])
C = np.dot(A,B)
print(C)
print(np.sin(C))
print()
print(C.T)
#  here T is transpose
