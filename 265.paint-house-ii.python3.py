#
# [265] Paint House II
#
# https://leetcode.com/problems/paint-house-ii/description/
#
# algorithms
# Hard (38.70%)
# Total Accepted:    32.4K
# Total Submissions: 83.8K
# Testcase Example:  '[[1,5,3],[2,9,4]]'
#
# There are a row of n houses, each house can be painted with one of the k
# colors. The cost of painting each house with a certain color is different.
# You have to paint all the houses such that no two adjacent houses have the
# same color.
#
# The cost of painting each house with a certain color is represented by a n x
# k cost matrix. For example, costs[0][0] is the cost of painting house 0 with
# color 0; costs[1][2] is the cost of painting house 1 with color 2, and so
# on... Find the minimum cost to paint all houses.
#
# Note:
# All costs are positive integers.
#
# Example:
#
#
# Input: [[1,5,3],[2,9,4]]
# Output: 5
# Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum
# cost: 1 + 4 = 5;
# Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 +
# 2 = 5.
#
#
# Follow up:
# Could you solve it in O(nk) runtime?
#


class Solution:
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if len(costs) == 0:
            return 0
        k = len(costs[0])
        dp = [[x for x in costs[0]] for y in range(2)]

        def _update(lr, rl, i):
            lr[0] = dp[i&1][0]
            for j in range(1, k):
                lr[j] = min(lr[j-1], dp[i&1][j])
            rl[k-1] = dp[i&1][k-1]
            for j in range(k-2, -1, -1):
                rl[j] = min(rl[j+1], dp[i&1][j])

        def _getmin(lr, rl, j):
            if j == 0:
                return rl[1]
            if j == k-1:
                return lr[k-2]
            return min(lr[j-1], rl[j+1])

        lr, rl = [0 for x in range(k)], [0 for x in range(k)]
        _update(lr, rl, 0)
        for i in range(1, len(costs)):
            for j in range(k):
                dp[i&1][j] = _getmin(lr, rl, j) + costs[i][j]
            _update(lr, rl, i)
        return min(dp[(len(costs)-1)&1])
