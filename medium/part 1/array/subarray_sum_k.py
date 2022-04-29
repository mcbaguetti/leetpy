"""560. Subarray Sum Equals K
Medium

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2

Example 2:
Input: nums = [1,2,3], k = 3
Output: 2


Constraints:
1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""


def calc_subarrays(nums, k):

    prefix_sum = {0: 1}
    res = 0
    curr_sum = 0

    for n in nums:
        curr_sum += n
        diff = curr_sum - k

        res += prefix_sum.get(diff, 0)
        prefix_sum[curr_sum] = 1 + prefix_sum.get(curr_sum, 0)

    return res
