"""345. Reverse Vowels of a String
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

Example 1
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"


Constraints:

    1 <= s.length <= 3 * 105
    s consist of printable ASCII characters.
"""


def reverseVowels(s: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    str_len = len(s)
    i = 0
    j = str_len - 1
    reversed_str = list(s)

    while i < j:
        if s[i] in vowels and s[j] in vowels:
            reversed_str[i] = s[j]
            reversed_str[j] = s[i]
            i += 1
            j -= 1

        if s[i] not in vowels:
            i += 1

        if s[j] not in vowels:
            j -= 1

    return "".join(reversed_str)


print(reverseVowels("prova"))
