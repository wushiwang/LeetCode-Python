#
# [188] Best Time to Buy and Sell Stock IV
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/
#
# algorithms
# Hard (25.08%)
# Total Accepted:    63.7K
# Total Submissions: 253.8K
# Testcase Example:  '2\n[2,4,1]'
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most k
# transactions.
#
# Note:
# You may not engage in multiple transactions at the same time (ie, you must
# sell the stock before you buy again).
#
# Example 1:
#
#
# Input: [2,4,1], k = 2
# Output: 2
# Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit =
# 4-2 = 2.
#
#
# Example 2:
#
#
# Input: [3,2,6,5,0,3], k = 2
# Output: 7
# Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit =
# 6-2 = 4.
# Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 =
# 3.
#


class Solution:
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if k >= (n >> 1):
            res = 0
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    res += prices[i]-prices[i-1]
            return res
        dp = [0 for y in range(k+1)]
        curMin = [prices[0] for y in range(k+1)]
        for j in range(1, n):
            for i in range(1, k+1):
                curMin[i] = min(curMin[i], prices[j]-dp[i-1])
                dp[i] = max(dp[i], prices[j]-curMin[i])
        return dp[k]
