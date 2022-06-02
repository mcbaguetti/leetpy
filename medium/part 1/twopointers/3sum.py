"""
15. 3Sum
Medium

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.



Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []


Constraints:
0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""


def find_three(nums):
    res = []
    nums.sort()

    for i, n in enumerate(nums):
        if i > 0 and n == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            three_sum = n + nums[l] + nums[r]
            if three_sum > 0:
                r -= 1
            elif three_sum < 0:
                l += 1
            else:
                res.append([n, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1

    return res


print(find_three([-1,0,1,2,-1,-4]))
