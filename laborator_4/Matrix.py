import numpy as np
'''Write a Python class that simulates a matrix of size NxM, with N and M provided at initialization.
The class should provide methods to access elements (get and set methods) and some methematical
functions such as transpose, matrix multiplication and a method that allows iterating through
all elements form a matrix an apply a transformation over them (via a lambda function).'''


class Matrix:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.matrix = np.zeros((N, M))

    def set_element(self, row, column, value):
        self.matrix[row][column] = value

    def get_element(self, row, column):
        return self.matrix[row][column]

    def print_matrix(self, matrix):
        if matrix is not None:
            for row in range(self.N):
                print(matrix[row])
        else:
            for row in range(self.N):
                print(self.matrix[row])

    def transpose(self):
        return self.matrix.transpose()

    def multiply_with(self, other_matrix):
        return np.matmul(self.matrix, other_matrix)

    def apply_function(self, function):
        return list(map(lambda x: function(x), [row for row in self.matrix]))
