#
# [416] Partition Equal Subset Sum
#
# https://leetcode.com/problems/partition-equal-subset-sum/description/
#
# algorithms
# Medium (38.67%)
# Total Accepted:    47.7K
# Total Submissions: 123.4K
# Testcase Example:  '[1,5,11,5]'
#
# Given a non-empty array containing only positive integers, find if the array
# can be partitioned into two subsets such that the sum of elements in both
# subsets is equal.
#
#
# Note:
#
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
#
#
#
# Example 1:
#
# Input: [1, 5, 11, 5]
#
# Output: true
#
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
#
#
#
# Example 2:
#
# Input: [1, 2, 3, 5]
#
# Output: false
#
# Explanation: The array cannot be partitioned into equal sum subsets.
#


class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        s = sum(nums)
        if s & 1 == 1:
            return False
        dp = set()
        dp.add(nums[0])
        for i in range(1, len(nums)):
            nxt = set()
            for n in dp:
                if n+nums[i] not in dp:
                    nxt.add(n+nums[i])
            dp |= nxt
            if (s >> 1) in dp:
                return True
        return False
