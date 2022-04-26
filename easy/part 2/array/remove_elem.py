"""
27. Remove Element
Easy

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
The relative order of the elements may be changed.
Since it is impossible to change the length of the array in some languages, you must instead have the result
be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates,
then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.
Return k after placing the final result in the first k slots of nums.
Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 3:
Input: nums = [0,1,2,2,3,0,4,2], val = 0
Output: 6, nums = [2,1,4,2,3,2,_,_]
"""


# 0(n^2) time complex
def remove_elem(nums, val):
    count = 0
    i = 0
    while i < len(nums):
        if nums[i] == val:
            j = i + 1

            while j < len(nums):
                if nums[j] != val:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp

                j += 1
        i += 1

    for elem in nums:
        if elem == val:
            count += 1

    return len(nums) - count


# 0(n) time complex
def remove_element_v2(nums, val):
    begin = 0
    i = 0
    while i < len(nums):
        if nums[i] != val:
            nums[begin] = nums[i]
            begin += 1
        i += 1

    return begin


# 0(n) time complex
def remove_elem_v3(nums, val):

    i = 0
    length = len(nums)

    while i < length:
        if nums[i] == val:
            nums[i] = nums[length - 1]
            length -= 1

        else:
            i += 1

    return length
