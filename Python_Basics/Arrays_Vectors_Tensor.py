import numpy as np
import matplotlib.pyplot as plt

vector = np.array([1,2,3,4])
print("The vector is \n" , vector)
print("")

matrix = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print("The matrix is \n", matrix)
print("")

tensor = np.array([
 
    [[1, 2, 3],[4, 5, 6],[7, 8, 9]],
    [[10,11, 12],[13, 14, 15],[16, 17, 18]],
    [[19, 20, 21],[22, 23, 24],[25, 26, 27]],
])
print("The tensor is \n", tensor)

plt.imshow(tensor, interpolation = 'nearest')
plt.show()