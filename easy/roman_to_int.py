"""13. Roman to Integer"""

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together.
# 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right.
# However, the numeral for four is not IIII. Instead, the number four is written as IV.
# Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX.
# There are six instances where subtraction is used:
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.
#
#
# Example 1:
# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.

def roman_to_int(string):
    roman_numbers = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    count = 0

    for i, elem in enumerate(string):
        if i != string.__len__() - 1:
            next_elem = string[i+1]
        else:
            count += roman_numbers[elem]
            print(count)
            return 0
        if roman_numbers[elem] >= roman_numbers[next_elem]:
            count += roman_numbers[elem]

        else:
            count -= roman_numbers[elem]

    print(count)


roman_to_int("III")
