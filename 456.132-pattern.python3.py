#
# [456] 132 Pattern
#
# https://leetcode.com/problems/132-pattern/description/
#
# algorithms
# Medium (27.68%)
# Total Accepted:    19.7K
# Total Submissions: 71.1K
# Testcase Example:  '[1,2,3,4]'
#
#
# Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a
# subsequence ai, aj, ak such
# that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n
# numbers as input and checks whether there is a 132 pattern in the list.
#
# Note: n will be less than 15,000.
#
# Example 1:
#
# Input: [1, 2, 3, 4]
#
# Output: False
#
# Explanation: There is no 132 pattern in the sequence.
#
#
#
# Example 2:
#
# Input: [3, 1, 4, 2]
#
# Output: True
#
# Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
#
#
#
# Example 3:
#
# Input: [-1, 3, 2, 0]
#
# Output: True
#
# Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1,
# 3, 0] and [-1, 2, 0].
#
import math


class Solution:
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        stack, s3 = [], -math.inf
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < s3:
                return True
            else:
                while len(stack) != 0 and nums[i] > stack[-1]:
                    s3 = max(s3, stack.pop())
            stack.append(nums[i])
        return False
