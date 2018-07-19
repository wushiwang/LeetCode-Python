#
# [503] Next Greater Element II
#
# https://leetcode.com/problems/next-greater-element-ii/description/
#
# algorithms
# Medium (48.24%)
# Total Accepted:    30.6K
# Total Submissions: 63.4K
# Testcase Example:  '[1,2,1]'
#
#
# Given a circular array (the next element of the last element is the first
# element of the array), print the Next Greater Number for every element. The
# Next Greater Number of a number x is the first greater number to its
# traversing-order next in the array, which means you could search circularly
# to find its next greater number. If it doesn't exist, output -1 for this
# number.
#
#
# Example 1:
#
# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; The number 2 can't find
# next greater number; The second 1's next greater number needs to search
# circularly, which is also 2.
#
#
#
# Note:
# The length of given array won't exceed 10000.
#


class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack, dic = [], dict()
        for i in range(2*len(nums)):
            while len(stack) != 0 and nums[i%len(nums)] > stack[-1][1]:
                cur = stack.pop()
                dic[cur[0]] = i%len(nums)
            if i < len(nums):
                stack.append((i, nums[i]))
        res = []
        for i in range(len(nums)):
            if i in dic:
                res.append(nums[dic[i]])
            else:
                res.append(-1)
        return res
