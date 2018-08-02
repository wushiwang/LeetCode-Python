#
# [645] Set Mismatch
#
# https://leetcode.com/problems/set-mismatch/description/
#
# algorithms
# Easy (39.74%)
# Total Accepted:    31.9K
# Total Submissions: 80.2K
# Testcase Example:  '[1,2,2,4]'
#
#
# The set S originally contains numbers from 1 to n. But unfortunately, due to
# the data error, one of the numbers in the set got duplicated to another
# number in the set, which results in repetition of one number and loss of
# another number.
#
#
#
# Given an array nums representing the data status of this set after the error.
# Your task is to firstly find the number occurs twice and then find the number
# that is missing. Return them in the form of an array.
#
#
#
# Example 1:
#
# Input: nums = [1,2,2,4]
# Output: [2,3]
#
#
#
# Note:
#
# The given array size will in the range [2, 10000].
# The given array's numbers won't have any order.
#


class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        miss1 = 0
        for i in range(len(nums)):
            while nums[i] != i+1:
                tmp = nums[i]
                if nums[tmp-1] != tmp:
                    nums[i] = nums[tmp-1]
                    nums[tmp-1] = tmp
                else:
                    miss1 = tmp
                    break
        for i in range(len(nums)):
            if nums[i] != i+1:
                return ([miss1, i+1])
