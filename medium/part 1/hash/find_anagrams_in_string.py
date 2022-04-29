"""
438. Find All Anagrams in a String
Medium

Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".


Constraints:
1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
"""


def find_anagrams(s, p):

    res = []
    p_dict = {}
    p_len = len(p)
    s_temp = {}

    if p_len > len(s):
        return res

    for letter in p:
        p_dict[letter] = 1 + p_dict.get(letter, 0)

    for i, letter in enumerate(s):
        s_temp[letter] = 1 + s_temp.get(letter, 0)

        if i >= p_len:
            first_lett = s[i - p_len]
            s_temp[first_lett] -= 1

            if s_temp[first_lett] == 0:
                del s_temp[first_lett]

        if s_temp == p_dict:
            res.append(i - p_len + 1)

    return res


print(find_anagrams("abab", "ab"))
