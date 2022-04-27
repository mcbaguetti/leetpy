"""121. Best Time to Buy and Sell Stock
Easy

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104"""


# too much time complexity O(n^2)
def max_profit(prices):
    profit = []
    i = 0

    while i < len(prices):
        j = i + 1
        while j < len(prices):
            if prices[j] - prices[i] > 0:
                profit.append(prices[j] - prices[i])
            j += 1

        i += 1

    if len(prices) <= 1 or len(profit) < 1 or max(profit) <= 0:
        return 0
    return max(profit)


print(max_profit([7, 2, 6, 3, 1, 4]))


# 0(n) time compl and 0(1) space compl
def maxProfit(prices):

    n = len(prices)
    ans = 0
    cur_sum = 0
    for i in range(n - 1):
        cur_sum += prices[i + 1] - prices[i]
        if cur_sum < 0:
            cur_sum = 0
        ans = max(ans, cur_sum)
    return ans
