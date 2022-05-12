"""240. Search a 2D Matrix II
Medium

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix.
This matrix has the following properties:
    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.


Example 1:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
Output: true

Example 2:
Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
Output: false
"""


# runtime 0(mlogn)
def find_target(matrix, target):
    if not len(matrix) or not len(matrix[0]):
        return False

    for row in matrix:
        left, right = 0, len(row) - 1

        while left <= right:
            middle = left + (right - left) // 2

            if row[middle] > target:
                right = middle - 1
            elif row[middle] < target:
                left = middle + 1
            else:
                return True

    return False


# runtime 0(m + n)
def find_target_v2(matrix, target):
    if not len(matrix) or not len(matrix[0]):
        # Quick response for empty matrix
        return False

    h, w = len(matrix), len(matrix[0])

    # Start adaptive search from bottom left corner
    y, x = h - 1, 0

    while True:

        if y < 0 or x >= w:
            break

        current = matrix[y][x]

        if target < current:
            # target is smaller, then go up
            y -= 1

        elif target > current:
            # target is larger, then go right
            x += 1

        else:
            # hit target
            return True

    return False

