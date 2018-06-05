#
# [123] Best Time to Buy and Sell Stock III
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
#
# algorithms
# Hard (30.61%)
# Total Accepted:    110.3K
# Total Submissions: 360.2K
# Testcase Example:  '[3,3,5,0,0,3,1,4]'
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most two
# transactions.
#
# Note: You may not engage in multiple transactions at the same time (i.e., you
# must sell the stock before you buy again).
#
# Example 1:
#
#
# Input: [3,3,5,0,0,3,1,4]
#         0 0 2 2 2 3 3 4
#         0 0 0 0 2 5 5 6
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit =
# 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 =
# 3.
#
# Example 2:
#
#
# Input: [1,2,3,4,5]
#         0 1 2 3 4
#         0 0 0 2 3
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit =
# 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you
# are
# engaging multiple transactions at the same time. You must sell before buying
# again.
#
#
# Example 3:
#
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
#


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        dp = [[0 for x in range(len(prices))] for y in range(2)]
        res, low = 0, prices[0]
        for i in range(1, len(prices)):
            dp[0][i] = max(dp[0][i], prices[i]-low)
            low = min(low, prices[i])
            res = max(res, dp[0][i])
        high = prices[-1]
        for i in range(len(prices)-2, 1, -1):
            dp[1][i] = max(dp[1][i+1], high-prices[i])
            high = max(high, prices[i])
            res = max(res, dp[1][i]+dp[0][i-1])
        return res
