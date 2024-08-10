"""Transpose means is to interchange rows and columns of a two-dimensional array matrix.

[AT]ij=[A]ji

ie: Formally, the i th row, j th column element of AT is the j th row, i th column element of A

Example :
[[1,2,3],[4,5,6]].transpose() //should return [[1,4],[2,5],[3,6]]
"""

# My solution

def transpose(arr):
    idx_counter = len(arr[0])
    transposed_matrix = []

    for i in range(idx_counter):
        new_column = []
        for j in arr:
            new_column.append(j[i])
        transposed_matrix.append(new_column)

    return transposed_matrix