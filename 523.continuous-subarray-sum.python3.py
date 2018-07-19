#
# [523] Continuous Subarray Sum
#
# https://leetcode.com/problems/continuous-subarray-sum/description/
#
# algorithms
# Medium (23.35%)
# Total Accepted:    38.2K
# Total Submissions: 163.5K
# Testcase Example:  '[23,2,4,6,7]\n6'
#
#
# Given a list of non-negative numbers and a target integer k, write a function
# to check if the array has a continuous subarray of size at least 2 that sums
# up to the multiple of k, that is, sums up to n*k where n is also an
# integer.
#
#
#
# Example 1:
#
# Input: [23, 2, 4, 6, 7],  k=6
# Output: True
# Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to
# 6.
#
#
#
#
# Example 2:
#
# Input: [23, 2, 6, 4, 7],  k=6
# Output: True
# Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and
# sums up to 42.
#
#
#
# Note:
#
# The length of the array won't exceed 10,000.
# You may assume the sum of all the numbers is in the range of a signed 32-bit
# integer.
#


class Solution:
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0:
            for i in range(1, len(nums)):
                if nums[i] == nums[i-1] == 0:
                    return True
            return False
        dic, cur = set(), 0
        for i in range(len(nums)):
            cur += nums[i]
            cur %= k
            if cur == 0 and i != 0:
                return True
            else:
                if cur not in dic:
                    dic.add(cur)
                else:
                    return True
        return False
