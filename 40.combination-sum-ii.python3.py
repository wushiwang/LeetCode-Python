#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (36.42%)
# Total Accepted:    155.1K
# Total Submissions: 425.5K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
# numbers sums to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note:
#
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
#
#
# Example 1:
#
#
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
#
#
# Example 2:
#
#
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
# [1,2,2],
# [5]
# ]
#


class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates, res, dic = sorted(candidates), list(), {}
        self.DFS(candidates, target, 0, res, list(), dic)
        return res

    def DFS(self, candidates, target, n, res, cur, dic):
        if target == 0:
            tmp = ''.join(list(map(str, cur)))
            if tmp not in dic:
                res.append(cur)
                dic[tmp] = True
            return
        if n == len(candidates) or candidates[n] > target:
            return
        self.DFS(candidates, target, n+1, res, cur, dic)
        self.DFS(candidates, target-candidates[n], n+1, res, cur+[candidates[n]], dic)
