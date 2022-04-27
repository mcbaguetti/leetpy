"""739. Daily Temperatures
Medium


Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i]
is the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]


Constraints:
1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""


# O(n^2) time complexity, too slow...
def check_warmer(temperatures):

    ans = []
    slow = 0

    while slow < len(temperatures):

        fast = slow

        while fast < len(temperatures):
            if fast == len(temperatures):
                ans.append(0)
                break

            if temperatures[fast] > temperatures[slow]:
                ans.append(fast - slow)
                break

            fast += 1

        if fast == len(temperatures):
            ans.append(0)

        slow += 1

    return ans


# improved version with O(n) time complex
def check_temp(temperatures):
    ans = [0] * len(temperatures)
    stack = []  # pair: [temp, index]

    for i, temp in enumerate(temperatures):
        while stack and temp > stack[-1][0]:
            stack_temp, stack_idx = stack.pop()
            ans[stack_idx] = i - stack_idx
        stack.append([temp, i])

    return ans


check_temp([76])
