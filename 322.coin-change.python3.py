#
# [322] Coin Change
#
# https://leetcode.com/problems/coin-change/description/
#
# algorithms
# Medium (26.76%)
# Total Accepted:    102.6K
# Total Submissions: 383.4K
# Testcase Example:  '[1,2,5]\n11'
#
# You are given coins of different denominations and a total amount of money
# amount. Write a function to compute the fewest number of coins that you need
# to make up that amount. If that amount of money cannot be made up by any
# combination of the coins, return -1.
#
# Example 1:
#
#
# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
#
# Example 2:
#
#
# Input: coins = [2], amount = 3
# Output: -1
#
#
# Note:
# You may assume that you have an infinite number of each kind of coin.
#
import math


class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [math.inf]*(amount+1)
        coins = sorted(coins)
        dp[0] = 0
        for i in range(1, amount+1):
            for v in coins:
                if i-v >= 0:
                    dp[i] = min(dp[i], dp[i-v]+1)
                else:
                    break
        return dp[amount] if dp[amount] != math.inf else -1
