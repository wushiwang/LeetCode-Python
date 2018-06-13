#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (26.97%)
# Total Accepted:    144.4K
# Total Submissions: 535.3K
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.
#
# Example 1:
#
#
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#
#
# Example 2:
#
#
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
#


class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return
        res = nums[0]
        L = H = None
        for i in range(len(nums)):
            if nums[i] > 0:
                L = L*nums[i] if L else None
                H = H*nums[i] if H else nums[i]
            elif nums[i] < 0:
                nL = H*nums[i] if H else nums[i]
                nH = L*nums[i] if L else None
                L, H = nL, nH
            else:
                res = max(res, 0)
                L = H = None
                continue
            if L:
                res = max(res, L)
            if H:
                res = max(res, H)
        return res
