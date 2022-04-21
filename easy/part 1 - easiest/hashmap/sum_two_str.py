"""415. Add Strings

Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"


Constraints:

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself."""


def sum_two_str(str1, str2):

    str_to_int = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    int_to_str = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}
    sum_str = ""
    num1 = 0
    num2 = 0

    if str1 == "0" and str2 == "0":
        return "0"

    for number in str1:
        num1 = num1 * 10 + str_to_int[number]

    for number in str2:
        num2 = num2 * 10 + str_to_int[number]

    tot_sum = num1 + num2

    while tot_sum > 0:
        rem = tot_sum % 10
        tot_sum = tot_sum // 10
        sum_str = int_to_str[rem] + sum_str

    return sum_str


res = sum_two_str("100", "10")
print(res)

