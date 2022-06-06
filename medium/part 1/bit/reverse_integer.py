"""7. Reverse Integer
Medium

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:
Input: x = 123
Output: 321

Example 2:
Input: x = -123
Output: -321

Example 3:
Input: x = 120
Output: 21


Constraints:
-231 <= x <= 231 - 1
"""


def reverse(x: int) -> int:
    num = ""
    sign = 1
    mask = 0x7FFFFFFF  # the max 32bit positive integer

    if x < 0:
        sign = -1
        x = -x

    if x > mask:
        return 0

    while x != 0:
        rem = x % 10
        x //= 10

        num += str(rem)

    if not num or int(num) > mask:
        return 0

    return int(num) * sign


# small optimization
def reverse2(x: int) -> int:
    num = 0
    sign = 1
    mask = 2147483648

    if x < 0:
        sign = -1
        x = -x

    if x > mask:
        return 0

    while x != 0:
        rem = x % 10
        x //= 10

        num = num * 10 + rem

    if not num or num > mask:
        return 0

    return num * sign
