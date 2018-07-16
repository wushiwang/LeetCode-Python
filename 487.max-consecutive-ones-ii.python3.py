#
# [487] Max Consecutive Ones II
#
# https://leetcode.com/problems/max-consecutive-ones-ii/description/
#
# algorithms
# Medium (45.41%)
# Total Accepted:    15.4K
# Total Submissions: 33.9K
# Testcase Example:  '[1,0,1,1,0,1]'
#
#
# Given a binary array, find the maximum number of consecutive 1s in this array
# if you can flip at most one 0.
#
#
# Example 1:
#
# Input: [1,0,1,1,0]
# Output: 4
# Explanation: Flip the first zero will get the the maximum number of
# consecutive 1s.
# ⁠   After flipping, the maximum number of consecutive 1s is 4.
#
#
#
# Note:
#
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000
#
#
#
# Follow up:
# What if the input numbers come in one by one as an infinite stream? In other
# words, you can't store all numbers coming from the stream as it's too large
# to hold in memory. Could you solve it efficiently?
#


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res, cur, pre, head = 0, 0, 0, True
        for i in range(len(nums)):
            if nums[i] == 1:
                cur += 1
                if head:
                    res = max(res, cur)
                else:
                    res = max(res, cur+1+pre)
            else:
                head = False
                if i != 0:
                    if nums[i-1] == 1:
                        pre = cur
                    else:
                        pre = 0
                res = max(res, 1+pre)
                cur = 0
        return res
