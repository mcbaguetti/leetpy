"""342. Power of Four
Easy

Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4x.

Example 1:
Input: n = 16
Output: true

Example 2:
Input: n = 5
Output: false

Example 3:
Input: n = 1
Output: true


Example 4:
Input: n = -16
Output: false


Constraints:

    -231 <= n <= 231 - 1

Follow up: Could you solve it without loops/recursion?
"""


# the interesting part of this problem is to solve it without recursion or loops
def is_power_of_four(n: int) -> bool:

    if n <= 0:
        return False

    if n == 1:
        return True

    str_bin = str(bin(n))
    sliced = str_bin[2:]
    num_zero = sliced.count('0')

    if int(sliced[0]) == 1 and num_zero % 2 == 0 and (len(sliced) - 1) == num_zero:
        return True

    return False


print(is_power_of_four(-2147483648))
