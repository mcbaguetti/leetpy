"""
74. Search a 2D Matrix
Medium

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix.
This matrix has the following properties:
    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.


Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false


Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""


# 0(logn + logm)
def find_target(matrix, target):

    top, bottom = 0, len(matrix) - 1
    row = 0

    while top <= bottom:
        row = (top + bottom) // 2

        if target < matrix[row][0]:
            bottom = row - 1
        elif target > matrix[row][-1]:
            top = row + 1
        else:
            break

    if not (top <= bottom):
        return False

    left, right = 0, len(matrix[0]) - 1

    while left <= right:
        col = (left + right) // 2

        if target < matrix[row][col]:
            right = col - 1
        elif target > matrix[row][col]:
            left = col + 1
        else:
            return True

    return False
