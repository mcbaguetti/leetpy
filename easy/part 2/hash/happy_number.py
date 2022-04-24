"""202. Happy Number
Easy

Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.


Example 1:
Input: n = 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Example 2:
Input: n = 2
Output: false


Constraints:
1 <= n <= 231 - 1
"""


# range(6) because at maximum in 6 steps we know if we reach 1 or 7
def happy_number(n):
    res = 0

    for _ in range(6):
        for digit in str(n):
            res += int(digit) ** 2

        n = res
        res = 0

        if n == 1 or n == 7:
            return True

    return False


# if n == 4 we know that we don't finish the loop
def happy_number_v2(n):
    res = 0

    if n == 1:
        return True

    while n != 1:
        for digit in str(n):
            res += int(digit) ** 2

        n = res
        res = 0

        if n == 1 or n == 7:
            return True

        if n == 4:
            return False


# with hash table for spotting the infinite loop
def happy_number_v3(n):
    res = 0
    save = {}

    if n == 1:
        return True

    while n != 1:
        for digit in str(n):
            res += int(digit) ** 2

        n = res
        res = 0
        if n not in save:
            save[n] = 1
        else:
            return False

        if n == 1 or n == 7:
            return True
