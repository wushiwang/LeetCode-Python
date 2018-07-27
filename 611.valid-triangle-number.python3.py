#
# [611] Valid Triangle Number
#
# https://leetcode.com/problems/valid-triangle-number/description/
#
# algorithms
# Medium (42.03%)
# Total Accepted:    21K
# Total Submissions: 50K
# Testcase Example:  '[2,2,3,4]'
#
# Given an array consists of non-negative integers,  your task is to count the
# number of triplets chosen from the array that can make triangles if we take
# them as side lengths of a triangle.
#
# Example 1:
#
# Input: [2,2,3,4]
# Output: 3
# Explanation:
# Valid combinations are:
# 2,3,4 (using the first 2)
# 2,3,4 (using the second 2)
# 2,2,3
#
#
#
# Note:
#
# The length of the given array won't exceed 1000.
# The integers in the given array are in the range of [0, 1000].
#


class Solution:
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums, res = sorted(nums, reverse=True), 0
        for c in range(len(nums)-2):
            b = c+1
            a = len(nums)-1
            while b < a:
                if nums[a] + nums[b] > nums[c]:
                    res += (a-b)
                    b += 1
                else:
                    a -= 1
        return res
