#Rotate Matrix
import numpy as np

myarray=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(myarray)

def rotatMatrix(matrix):
    n=len(matrix)
    for layer in range(n//2):
        first=layer
        last=n-layer-1
        for i in range(first,last):
            # save top
            top = matrix[layer][i]

            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]

            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]

            # top -> right
            matrix[i][- layer - 1] = top
    return matrix

print(rotatMatrix(myarray))