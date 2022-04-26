"""118. Pascal's Triangle
Easy

Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]


Constraints:
1 <= numRows <= 30
"""


def pascal_rows(rows):
    ans = []

    for i in range(rows + 1):
        row_list = []
        for j in range(i):
            if j == 0 or j == i - 1:
                row_list.append(1)
            else:
                row_list.append(ans[i - 1][j - 1] + ans[i - 1][j])

        ans.append(row_list)

    del ans[0]
    return ans


print(pascal_rows(5))


# alternative version
def generate(self, rows):
    ans = [[1] * i for i in range(1, rows + 1)]  # initialize triangle with all 1
    for i in range(1, rows):
        for j in range(1, i):
            ans[i][j] = ans[i - 1][j] + ans[i - 1][j - 1]  # update each as sum of two elements from above row
    return ans
