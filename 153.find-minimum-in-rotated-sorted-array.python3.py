#
# [153] Find Minimum in Rotated Sorted Array
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (41.11%)
# Total Accepted:    201.7K
# Total Submissions: 490.6K
# Testcase Example:  '[3,4,5,1,2]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
#
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.
#
# Example 1:
#
#
# Input: [3,4,5,1,2]
# Output: 1
#
#
# Example 2:
#
#
# Input: [4,5,6,7,0,1,2]
# Output: 0
#


class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return
        L, R = 0, len(nums)-1
        while L < R - 1:
            M = (L + R) >> 1
            if nums[M] > nums[L]:
                L = M
            else:
                R = M
        res = L if nums[L] > nums[R] else R
        return nums[(res+1) % len(nums)]
