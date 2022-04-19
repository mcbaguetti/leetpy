from typing import List

"""Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.

 
Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

"""


# first solution, time complexity O(n*m)
def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    i = 0
    out = []
    while i < len(nums1):
        if nums1[i] in nums2 and nums1[i] not in out:
            out.append(nums1[i])

        i += 1
    return out


# improved version with augmented space complexity but better time complexity O(n + m)
def intersection_better(self, nums1: List[int], nums2: List[int]) -> List[int]:
    i = 0
    out = []
    res = {}

    while i < len(nums1):
        res[nums1[i]] = 1
        i += 1

    i = 0
    while i < len(nums2):
        if nums2[i] in res and res[nums2[i]]:
            res[nums2[i]] -= 1
            out.append(nums2[i])
        i += 1

    return out
