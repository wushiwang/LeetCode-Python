#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (45.56%)
# Total Accepted:    241.8K
# Total Submissions: 530.8K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
#
# Input: nums = [1,2,3]
# Output:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
#


class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.DFS(0, nums, res, [])
        return res

    def DFS(self, level, nums, res, cur):
        if level == len(nums):
            res.append(cur)
            return
        self.DFS(level+1, nums, res, cur)
        self.DFS(level+1, nums, res, cur+[nums[level]])
