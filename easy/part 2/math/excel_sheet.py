"""171. Excel Sheet Column Number
Easy


Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
...


Example 1:
Input: columnTitle = "A"
Output: 1

Example 2:
Input: columnTitle = "AB"
Output: 28

Example 3:
Input: columnTitle = "ZY"
Output: 701


Constraints:
1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].
"""


# you can use ord(char) if you don't want to use dictionary
def find_column_num(column_name):
    conv_dict = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5,
                 "F": 6, "G": 7, "H": 8, "I": 9, "J": 10,
                 "K": 11, "L": 12, "M": 13, "N": 14, "O": 15,
                 "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20,
                 "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25,
                 "Z": 26}

    ans = 0
    i = 1
    pow_exp = 0
    base = 26
    len_col = len(column_name)

    # we could use one less variable because (i = pow + 1) if we want but I think it's clearer like this
    while i <= len_col:
        ans += conv_dict[column_name[len_col - i]] * (base ** pow_exp)
        pow_exp += 1
        i += 1

    return ans


print(find_column_num("ZY"))
