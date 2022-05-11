# 409 Longest_Palindrome:

# Given a string s which consists of lowercase or uppercase letters,
# return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.


def max_palindrome(s):

    res = 1
    counts = {}

    for char in s:
        counts[char] = 1 + counts.get(char, 0)

    print(counts)
    for elem in counts:
        res += (counts[elem] // 2) * 2

    if res > len(s):
        return res - 1

    return res


num = max_palindrome("acssssccbdra")
print(num)


def max_palindrome_v2(string):
    res = 1
    letters = {}

    for l in string:
        if l in letters:
            letters[l] += 1

            if letters[l] % 2 == 0:
                res += 2
        else:
            letters[l] = 1

    if res > len(string):
        return res - 1

    return res


# print(max_palindrome_v2("sssscc"))
