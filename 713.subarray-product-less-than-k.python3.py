#
# [713] Subarray Product Less Than K
#
# https://leetcode.com/problems/subarray-product-less-than-k/description/
#
# algorithms
# Medium (33.28%)
# Total Accepted:    13.6K
# Total Submissions: 40.9K
# Testcase Example:  '[10,5,2,6]\n100'
#
# Your are given an array of positive integers nums.
# Count and print the number of (contiguous) subarrays where the product of all
# the elements in the subarray is less than k.
#
# Example 1:
#
# Input: nums = [10, 5, 2, 6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are: [10], [5],
# [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
# Note that [10, 5, 2] is not included as the product of 100 is not strictly
# less than k.
#
#
#
# Note:
# 0 < nums.length .
# 0 < nums[i] < 1000.
# 0 .
#


class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k <= 1:
            return 0
        L, R = 0, 0
        res = 0
        cur = nums[0]
        while R < len(nums):
            while cur >= k:
                cur //= nums[L]
                L += 1
            res += R - L + 1
            R += 1
            if R < len(nums):
                cur *= nums[R]
        return res
