#
# [518] Coin Change 2
#
# https://leetcode.com/problems/coin-change-2/description/
#
# algorithms
# Medium (36.23%)
# Total Accepted:    17.2K
# Total Submissions: 47.3K
# Testcase Example:  '5\n[1,2,5]'
#
# You are given coins of different denominations and a total amount of money.
# Write a function to compute the number of combinations that make up that
# amount. You may assume that you have infinite number of each kind of coin.
#
# Note: You can assume that
#
#
# 0 <= amount <= 5000
# 1 <= coin <= 5000
# the number of coins is less than 500
# the answer is guaranteed to fit into signed 32-bit integer
#
#
#
#
# Example 1:
#
#
# Input: amount = 5, coins = [1, 2, 5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1
#
#
#
#
# Example 2:
#
#
# Input: amount = 3, coins = [2]
# Output: 0
# Explanation: the amount of 3 cannot be made up just with coins of 2.
#
#
#
#
# Example 3:
#
#
# Input: amount = 10, coins = [10]
# Output: 1
#


class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        coins = sorted(coins)
        dp = [[0 for x in range(amount+1)] for y in range(2)]
        dp[0][0] = 1
        for i in range(1, len(coins)+1):
            dp[i&1][0] = 1
            for j in range(1, amount+1):
                if j >= coins[i-1]:
                    dp[i&1][j] = dp[(i-1)&1][j] + dp[i&1][j-coins[i-1]]
                else:
                    dp[i&1][j] = dp[(i-1)&1][j]
        return dp[len(coins)&1][amount]
