"""290. Word Pattern
Easy

Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false


Constraints:
1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space."""


def check_pattern(pattern, s):
    match_dict = {}

    # if I can't use split function
    """
    word = []
    words = []
    space = " "
    
    i = 0
    while i < len(s):
        if s[i] == space:
            words.append("".join(word))
            word = []
            i += 1

        if i == len(s) - 1:
            word.append(s[i])
            words.append("".join(word))
            break

        word.append(s[i])
        i += 1
    """

    words = s.split()

    if len(pattern) != len(words):
        return False

    if len(set(pattern)) != len(set(words)):
        return False

    i = 0
    while i < len(pattern):
        if pattern[i] not in match_dict:
            match_dict[pattern[i]] = words[i]

        elif match_dict[pattern[i]] != words[i]:
            return False

        i += 1

    return True


print(check_pattern("abba", "dog dog dog dog"))


