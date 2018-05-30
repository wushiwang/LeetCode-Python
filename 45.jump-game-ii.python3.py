#
# [45] Jump Game II
#
# https://leetcode.com/problems/jump-game-ii/description/
#
# algorithms
# Hard (26.09%)
# Total Accepted:    117.9K
# Total Submissions: 451.9K
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
#
# Each element in the array represents your maximum jump length at that
# position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# Example:
#
#
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
# ⁠   Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
# Note:
#
# You can assume that you can always reach the last index.
#


class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        R, rec = 0, [0 for x in range(len(nums))]
        for i in range(len(nums)):
            if nums[i]+i >= len(nums)-1:
                return rec[i]+1
            for j in range(R+1, nums[i]+i+1):
                rec[j] = rec[i]+1
            R = max(R, nums[i]+i)
        return 0
