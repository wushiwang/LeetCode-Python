#
# [216] Combination Sum III
#
# https://leetcode.com/problems/combination-sum-iii/description/
#
# algorithms
# Medium (47.75%)
# Total Accepted:    92.1K
# Total Submissions: 192.8K
# Testcase Example:  '3\n7'
#
#
# Find all possible combinations of k numbers that add up to a number n, given
# that only numbers from 1 to 9 can be used and each combination should be a
# unique set of numbers.
#
# Note:
#
#
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
#
#
# Example 1:
#
#
# Input: k = 3, n = 7
# Output: [[1,2,4]]
#
#
# Example 2:
#
#
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]
#


class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums = [x for x in range(1, 10)]
        res = []
        self.DFS(nums, [], 0, res, k, n, 0)
        return res

    def DFS(self, nums, cur, s, res, k, n, pos):
        if len(cur) == k:
            if s == n:
                res.append(cur)
            return
        for i in range(pos, len(nums)):
            self.DFS(nums, cur+[nums[i]], s+nums[i], res, k, n, i+1)
