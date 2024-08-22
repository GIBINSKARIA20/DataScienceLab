import numpy as np
n=np.random.randint(10,size=(2,2))
print(n)


print("determinanat")
print(np.linalg.det(n))

print("inverse")
print(np.linalg.inv(n))

print("matrix rank")
print(np.linalg.matrix_rank(n))

                                     OUTPUT

[[15 10]
 [16 11]]
determinanat
4.999999999999999
inverse
[[ 2.2 -2. ]
 [-3.2  3. ]]
matrix rank
2
