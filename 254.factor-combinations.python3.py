#
# [254] Factor Combinations
#
# https://leetcode.com/problems/factor-combinations/description/
#
# algorithms
# Medium (43.83%)
# Total Accepted:    39.9K
# Total Submissions: 90.9K
# Testcase Example:  '1'
#
# Numbers can be regarded as product of its factors. For example,
#
#
# 8 = 2 x 2 x 2;
# ⁠ = 2 x 4.
#
#
# Write a function that takes an integer n and return all possible combinations
# of its factors.
#
# Note:
#
#
# You may assume that n is always positive.
# Factors should be greater than 1 and less than n.
#
#
# Example 1:
#
#
# Input: 1
# Output: []
#
#
# Example 2:
#
#
# Input: 37
# Output:[]
#
# Example 3:
#
#
# Input: 12
# Output:
# [
# ⁠ [2, 6],
# ⁠ [2, 2, 3],
# ⁠ [3, 4]
# ]
#
# Example 4:
#
#
# Input: 32
# Output:
# [
# ⁠ [2, 16],
# ⁠ [2, 2, 8],
# ⁠ [2, 2, 2, 4],
# ⁠ [2, 2, 2, 2, 2],
# ⁠ [2, 4, 4],
# ⁠ [4, 8]
# ]
#
import math


class Solution:
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.DFS(n, res, [])
        return res

    def DFS(self, n, res, cur):
        start = 2 if len(cur) == 0 else cur[-1]
        for i in range(start, math.floor(math.sqrt(n))+1):
            if n % i == 0:
                res.append(cur+[i, n//i])
                self.DFS(n//i, res, cur+[i])
