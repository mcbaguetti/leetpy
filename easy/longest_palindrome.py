# Longest_Palindrome:
# Given a string s which consists of lowercase or uppercase letters,
# return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.


def max_palindrome(string):

    max_pal = 0
    first = True
    counts = {}

    for char in string:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    for elem in counts:

        if counts[elem] % 2 != 0 and first:
            max_pal += counts[elem]
            first = False

        else:
            max_pal += int(counts[elem] / 2) * 2

    return max_pal


num = max_palindrome("acssssccbdra")
print(num)
