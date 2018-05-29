#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (41.95%)
# Total Accepted:    224K
# Total Submissions: 533.5K
# Testcase Example:  '[2,3,6,7]\n7'
#
# Given a set of candidate numbers (candidates) (without duplicates) and a
# target number (target), find all unique combinations in candidates where the
# candidate numbers sums to target.
#
# The same repeated number may be chosen from candidates unlimited number of
# times.
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
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
#
#
# Example 2:
#
#
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
#


class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates, res = sorted(candidates), list()
        self.DFS(candidates, target, res, list(), 0)
        return res

    def DFS(self, candidates, target, res, cur, n):
        if target == 0:
            res.append(cur)
            return
        if n == len(candidates):
            return
        tmp = list()
        for i in range((target//candidates[n])+1):
            tmp.append(candidates[n])
            self.DFS(candidates, target-i*candidates[n], res, cur+tmp[:-1], n+1)
