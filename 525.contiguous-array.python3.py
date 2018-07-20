#
# [525] Contiguous Array
#
# https://leetcode.com/problems/contiguous-array/description/
#
# algorithms
# Medium (41.68%)
# Total Accepted:    27.7K
# Total Submissions: 66.3K
# Testcase Example:  '[0,1]'
#
# Given a binary array, find the maximum length of a contiguous subarray with
# equal number of 0 and 1.
#
#
# Example 1:
#
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0
# and 1.
#
#
#
# Example 2:
#
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal
# number of 0 and 1.
#
#
#
# Note:
# The length of the given binary array will not exceed 50,000.
#


class Solution:
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic, cur, res = dict(), 0, 0
        for i in range(len(nums)):
            cur  = cur + 1 if nums[i] == 1 else cur - 1
            if cur == 0:
                res = max(res, i+1)
            else:
                if cur not in dic:
                    dic[cur] = i
                else:
                    res = max(res, i-dic[cur])
        return res
