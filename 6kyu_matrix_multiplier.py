"""Challenge description

To complete this kata, write a function that takes two matrices - a and b -
and returns the dot product of those matrices.
If the matrices cannot be multiplied, return null/None/Nothing or similar.

Each matrix will be represented by a two-dimensional list (a list of lists).
Each inner list will contain one or more numbers, representing a row in the matrix.

For example, the following matrix:

|1 2|
|3 4|

Would be represented as:

[[1, 2], [3, 4]]"""

# My solution

def get_matrix_product(a, b):
    amount_cols_a = len(a[0])
    amount_rows_a = len(a)
    amount_rows_b = len(b)
    amount_cols_b = len(b[0])

    if amount_cols_a != amount_rows_b:
        return None

    matrix_c = [[0 for i in range(amount_cols_b)] for i in range(amount_rows_a)]
    print(matrix_c)

    for i in range(amount_rows_a):

        for j in range(amount_cols_b):
            total_sum = 0

            for k in range(amount_cols_a):
                temp_sum = a[i][k] * b[k][j]
                total_sum += temp_sum

            matrix_c[i][j] = total_sum

    return matrix_c