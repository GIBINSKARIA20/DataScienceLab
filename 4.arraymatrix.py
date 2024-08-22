import numpy as np
ar1  = np.array(([1,2],[3,4]))
ar2  = np.array(([5,6],[7,8]))
print(ar1)
print(ar2)

print("matrix addition")
print(np.add(ar1,ar2))

print("matrix substraction")
print(np.subtract(ar1,ar2))

print("matrix division")
print(np.divide(ar1,ar2))

print("matrix multiplication")
print(np.dot(ar1,ar2))

print("matrix transpose")
print(ar1.transpose())

print("sum of diagonal element of matrix")
print(np.trace(ar1))
