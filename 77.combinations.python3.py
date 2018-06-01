#
# [77] Combinations
#
# https://leetcode.com/problems/combinations/description/
#
# algorithms
# Medium (41.85%)
# Total Accepted:    147.2K
# Total Submissions: 351.7K
# Testcase Example:  '4\n2'
#
# Given two integers n and k, return all possible combinations of k numbers out
# of 1 ... n.
#
# Example:
#
#
# Input: n = 4, k = 2
# Output:
# [
# ⁠ [2,4],
# ⁠ [3,4],
# ⁠ [2,3],
# ⁠ [1,2],
# ⁠ [1,3],
# ⁠ [1,4],
# ]
#


class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = list()
        for i in range(1, n+1):
            self.DFS(k, 1, res, [i], n)
        return res

    def DFS(self, k, level, res, cur, n):
        if k == level:
            res.append(cur)
            return
        for i in range(cur[-1]+1, n+1):
            if n - i + 1 >= k - level:
                self.DFS(k, level+1, res, cur+[i], n)
