#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (38.64%)
# Total Accepted:    149.3K
# Total Submissions: 386.1K
# Testcase Example:  '[1,2,2]'
#
# Given a collection of integers that might contain duplicates, nums, return
# all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
#
# Input: [1,2,2]
# Output:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
#
import collections


class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        cnt, res = list(collections.Counter(nums).items()), []
        self.DFS(0, cnt, res, [])
        return res

    def DFS(self, level, cnt, res, cur):
        if level == len(cnt):
            res.append(cur)
            return
        for i in range(cnt[level][1]+1):
            self.DFS(level+1, cnt, res, cur+[cnt[level][0]]*i)
