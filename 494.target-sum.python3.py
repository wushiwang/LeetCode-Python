#
# [494] Target Sum
#
# https://leetcode.com/problems/target-sum/description/
#
# algorithms
# Medium (43.94%)
# Total Accepted:    58.8K
# Total Submissions: 133.8K
# Testcase Example:  '[1,1,1,1,1]\n3'
#
#
# You are given a list of non-negative integers, a1, a2, ..., an, and a target,
# S. Now you have 2 symbols + and -. For each integer, you should choose one
# from + and - as its new symbol.
# ⁠
#
# Find out how many ways to assign symbols to make sum of integers equal to
# target S.
#
#
# Example 1:
#
# Input: nums is [1, 1, 1, 1, 1], S is 3.
# Output: 5
# Explanation:
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# There are 5 ways to assign symbols to make the sum of nums be target 3.
#
#
#
# Note:
#
# The length of the given array is positive and will not exceed 20.
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.
#


class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.s, cur = [0]*len(nums), 0
        for i in range(len(nums)):
            cur += nums[i]
            self.s[i] = cur
        self.dic = dict()
        return self.DFS(nums, 0, 0, S)

    def DFS(self, nums, pos, cur, S):
        if pos == len(nums):
            if cur == S:
                return 1
            return 0
        if (pos, cur) in self.dic:
            return self.dic[(pos, cur)]
        rest = self.s[-1] - self.s[pos] + nums[pos]
        if (S - cur > 0 and rest < S - cur) or (S - cur < 0 and -rest > S - cur):
            self.dic[(pos, cur)] = 0
            return 0
        res = self.DFS(nums, pos+1, cur+nums[pos], S) + self.DFS(nums, pos+1, cur-nums[pos], S)
        self.dic[(pos, cur)] = res
        return res
