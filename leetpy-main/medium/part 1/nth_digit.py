""" 400 - Nth digit
Given an integer n, return the nth digit of the infinite integer sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].

Example 1:
Input: n = 3
Output: 3

Example 2:
Input: n = 11
Output: 0
Explanation: The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0,
which is part of the number 10.

Example 3:
Input: n = 15
Output: 2

Constraints:
    1 <= n <= 231 - 1

"""


# my first solution is ok but the time complexity is too much
def find_nth_digit(n):
    digit = []

    if n < 10:
        return n

    i = 1
    while i <= n:
        if i < 10:
            digit.append(i)
        else:
            digit_str = str(i)
            k = 0
            while k < len(digit_str):
                digit.append(int(digit_str[k]))
                k += 1
        i += 1

    return digit[n - 1]


# the ideal solution, much faster, it involves the structure of the problem.
# To make the problem much much more easier, I divide the problem into 3 parts:
#
#     calculate how many digits the number has.
#     calculate what the number is.
#     find out which digit in the number is we wanted.
#
# You can find the relative code part in the code section.
# Here is an example to help you to understand my code:
#
# Example:
#
#     Input: 250
#
#     After step 1, you will find that the 250th digit must belong to a 3-digit number, since 1~9 can only provide
#     9 digits and 10~99 can only provide 180 digits. Here, n = 250 - 9 - 90 * 2 = 61, and digits = 3.
#
#     In step 2, we will find the target number, which named as number in my code. From step 1, the n becomes to 61,
#     which means "the 61st digit in 3-digit number is the digit we are looking for ."
#     Easily, we know the 61st digit in 3-digit number belongs to number = 100 + 61 / 3 = 100 + 20 = 120.
#     index is the index of the target digit in number. If index equals to 0,
#     it means the target digit is the last digit of number.
#
#     Step 3, from step 2, we know index = n % digits = 61 % 3 = 1,
#     which means the target digit is the 1st digit in number. Then, return 1.

def findNthDigit(n: int):
    digit = 1
    base = 1

    if n < 10:
        return n

    while n > 9 * digit * base:
        n -= 9 * digit * base
        base *= 10
        digit += 1

    q, r = divmod(n - 1, digit)
    return int(str(q + base)[r])

