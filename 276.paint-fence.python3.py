#
# [276] Paint Fence
#
# https://leetcode.com/problems/paint-fence/description/
#
# algorithms
# Easy (35.02%)
# Total Accepted:    33.8K
# Total Submissions: 96.6K
# Testcase Example:  '3\n2'
#
# There is a fence with n posts, each post can be painted with one of the k
# colors.
#
# You have to paint all the posts such that no more than two adjacent fence
# posts have the same color.
#
# Return the total number of ways you can paint the fence.
#
# Note:
# n and k are non-negative integers.
#
# Example:
#
#
# Input: n = 3, k = 2
# Output: 6
# Explanation: Take c1 as color 1, c2 as color 2. All possible ways
# are:
#
# post1  post2  post3
# ⁠-----      -----  -----  -----
# ⁠  1         c1     c1     c2
# 2         c1     c2     c1
# 3         c1     c2     c2
# 4         c2     c1     c1 
# ⁠  5         c2     c1     c2
# 6         c2     c2     c1
#
# n = 1 -> k 2 3
# n = 2 -> k*k 4 9
# n = 3 -> k*k*k - k 6
# n = 4 -> k*dp[n-1] - 2 10
# n = 5 -> k*5 - 4 16
# n = 6 -> 32 - 6


class Solution:
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n == 1:
            return k
        dif = k * (k-1)
        same = k
        for i in range(3, n+1):
            tmp = dif
            dif = (dif+same)*(k-1)
            same = tmp
        return same+dif
