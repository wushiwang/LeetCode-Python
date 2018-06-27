#
# [309] Best Time to Buy and Sell Stock with Cooldown
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
#
# algorithms
# Medium (42.30%)
# Total Accepted:    64.5K
# Total Submissions: 152.4K
# Testcase Example:  '[1,2,3,0,2]'
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many
# transactions as you like (ie, buy one and sell one share of the stock
# multiple times) with the following restrictions:
#
#
# You may not engage in multiple transactions at the same time (ie, you must
# sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1
# day)
#
#
# Example:
#
#
# Input: [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
#


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        dp = [0]*(len(prices)+1)
        dp[0] = dp[1] = 0
        i, maxx = 2, -prices[0]
        while i <= len(prices):
            dp[i] = max(dp[i], dp[i-1], prices[i-1]+maxx)
            if i >= 2:
                maxx = max(maxx, dp[i-2]-prices[i-1])
            else:
                maxx = max(maxx, -prices[i-1])
            i += 1
        return dp[-1]
