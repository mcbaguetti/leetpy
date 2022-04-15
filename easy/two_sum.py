"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


"""


def two_sum(nums, target):

    output = []
    i = 0
    dictionary = {}

    while i < len(nums):

        if nums[i] > target:
            i += 1
            continue

        if nums[i] not in dictionary:
            dictionary[nums[i]] = i
            complem = target - nums[i]

            if complem not in dictionary:
                i += 1
                continue

            else:
                j = dictionary[complem]
                if j != i:
                    output.append(i)
                    output.append(j)
                    return output

        i += 1


input_list = [3, 3]
print(two_sum(input_list, 6))

