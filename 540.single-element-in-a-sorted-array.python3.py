#
# [540] Single Element in a Sorted Array
#
# https://leetcode.com/problems/single-element-in-a-sorted-array/description/
#
# algorithms
# Medium (56.10%)
# Total Accepted:    34.9K
# Total Submissions: 62.2K
# Testcase Example:  '[1,1,2]'
#
#
# Given a sorted array consisting of only integers where every element appears
# twice except for one element which appears once. Find this single element
# that appears only once.
#
#
# Example 1:
#
# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
#
#
#
# Example 2:
#
# Input: [3,3,7,7,10,11,11]
# Output: 10
#
#
#
# Note:
# Your solution should run in O(log n) time and O(1) space.
#


class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Binary Search
        L, R = 0, len(nums)-1
        while L < R:
            M = (L+R) >> 1
            if nums[M] != nums[M-1] and nums[M] != nums[M+1]:
                return nums[M]
            else:
                if nums[M] != nums[M-1]:
                    M -= 1
                if (M+1) & 1 == 0:
                    L = M+1
                else:
                    R = M
        return nums[R]
