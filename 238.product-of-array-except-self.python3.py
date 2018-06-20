#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (50.73%)
# Total Accepted:    157.7K
# Total Submissions: 310.8K
# Testcase Example:  '[1,2,3,4]'
#
# Given an array nums of n integers where n > 1,  return an array output such
# that output[i] is equal to the product of all the elements of nums except
# nums[i].
#
# Example:
#
#
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
#
#
# Note: Please solve it without division and in O(n).
#
# Follow up:
# Could you solve it with constant space complexity? (The output array does not
# count as extra space for the purpose of space complexity analysis.)
#


class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return []
        res = [1 for x in range(len(nums))]
        cur = nums[0]
        for i in range(1, len(nums)):
            res[i] = cur
            cur *= nums[i]
        cur = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            res[i] *= cur
            cur *= nums[i]
        return res
