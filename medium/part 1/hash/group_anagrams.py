"""
49. Group Anagrams
Medium


Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]


Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""


# time complex is 0(m * n) where m is the number of the strings and n is the avg length of the strings
def group_anagrams(strs):

    ans = {}

    for s in strs:
        count = [0] * 26  # from a to z

        for letter in s:
            count[ord(letter) - ord("a")] += 1

        if tuple(count) not in ans:
            ans[tuple(count)] = []
        ans[tuple(count)].append(s)

    return ans.values()


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
