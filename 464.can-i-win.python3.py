#
# [464] Can I Win
#
# https://leetcode.com/problems/can-i-win/description/
#
# algorithms
# Medium (25.91%)
# Total Accepted:    23.7K
# Total Submissions: 91.5K
# Testcase Example:  '10\n11'
#
# In the "100 game," two players take turns adding, to a running total, any
# integer from 1..10. The player who first causes the running total to reach or
# exceed 100 wins.
#
# What if we change the game so that players cannot re-use integers?
#
# For example, two players might take turns drawing from a common pool of
# numbers of 1..15 without replacement until they reach a total >= 100.
#
# Given an integer maxChoosableInteger and another integer desiredTotal,
# determine if the first player to move can force a win, assuming both players
# play optimally.
#
# You can always assume that maxChoosableInteger will not be larger than 20 and
# desiredTotal will not be larger than 300.
#
#
# Example
#
# Input:
# maxChoosableInteger = 10
# desiredTotal = 11
#
# Output:
# false
#
# Explanation:
# No matter which integer the first player choose, the first player will lose.
# The first player can choose an integer from 1 up to 10.
# If the first player choose 1, the second player can only choose integers from
# 2 up to 10.
# The second player will win by choosing 10 and get a total = 11, which is >=
# desiredTotal.
# Same with other integers chosen by the first player, the second player will
# always win.
#


class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        s = (maxChoosableInteger+1)*maxChoosableInteger / 2
        if s < desiredTotal:
            return False
        if desiredTotal <= 0:
            return True
        self.dic = dict()
        return self.DFS(0, maxChoosableInteger, desiredTotal)

    def DFS(self, stat, m, n):
        if n <= 0:
            return False
        if stat in self.dic:
            return self.dic[stat]
        for i in range(m, 0, -1):
            if (stat >> i) & 1 == 0:
                if not self.DFS(stat | (1 << i), m, n-i):
                    self.dic[stat] = True
                    return True
        self.dic[stat] = False
        return False
