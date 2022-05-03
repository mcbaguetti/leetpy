"""
347. Top K Frequent Elements
Medium

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


"""


# time and space complex 0(n)
def top_k_freq_elem(nums, k):

    dictionary = {}
    freq = [[] for _ in range(len(nums) + 1)]
    res = []

    for n in nums:
        dictionary[n] = 1 + dictionary.get(n, 0)

    for elem in dictionary:
        freq[dictionary[elem]].append(elem)

    i = len(freq) - 1
    while k > 0:
        for n in freq[i]:
            res.append(n)
            k -= 1
        i -= 1

    return res


print(top_k_freq_elem([1, 1, 1, 2, 2, 3], 2))
