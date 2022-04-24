"""169. Majority Element
Easy

Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2


Constraints:
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109


Follow-up: Could you solve the problem in linear time and in O(1) space?"""


# solution with O(n) time and space complexity
def majorityElement(self, nums: List[int]) -> int:
    count_dict = {}

    for elem in nums:
        if elem not in count_dict:
            count_dict[elem] = 1
        else:
            count_dict[elem] += 1

        if count_dict[elem] >= len(nums) / 2:
            return elem


# solution with O(n) time and 0(1) space complexity
def majorityElement(self, nums: List[int]) -> int:
    majority = nums[0]
    count = 1

    for elem in nums[1:]:
        if elem != majority:
            count -= 1

        else:
            count += 1

        if count == 0:
            majority = elem
            count = 1

    return majority