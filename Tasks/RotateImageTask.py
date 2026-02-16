def rotate(self, matrix: list[list[int]]):
    """
    Do not return anything, modify matrix in-place instead.
    """

    how_many_columns = len(matrix[0])


    for col in range(how_many_columns):

        for row in range(col):

            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    for col in range(len(matrix)):
        matrix[col].reverse()

    return matrix

#https://leetcode.com/problems/rotate-image/description/
