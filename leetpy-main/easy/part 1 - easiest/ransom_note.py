"""383. Ransom Note
Easy

Given two strings ransomNote and magazine, return true if ransomNote can be constructed from magazine and
false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true


Constraints:
    1 <= ransomNote.length, magazine.length <= 105
    ransomNote and magazine consist of lowercase English letters.

"""


def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    rans_dict = {}
    mag_dict = {}
    i = 0

    while i < len(ransomNote):
        if ransomNote[i] not in rans_dict:
            rans_dict[ransomNote[i]] = 1
        else:
            rans_dict[ransomNote[i]] += 1

        i += 1

    i = 0
    while i < len(magazine):

        if magazine[i] not in mag_dict:
            mag_dict[magazine[i]] = 1
        else:
            mag_dict[magazine[i]] += 1
        i += 1

    for elem in rans_dict:
        if elem not in mag_dict:
            return False
        else:
            if rans_dict[elem] > mag_dict[elem]:
                return False

    return True
