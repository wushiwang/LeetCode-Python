#
# [228] Summary Ranges
#
# https://leetcode.com/problems/summary-ranges/description/
#
# algorithms
# Medium (32.66%)
# Total Accepted:    102.5K
# Total Submissions: 313.7K
# Testcase Example:  '[0,1,2,4,5,7]'
#
# Given a sorted integer array without duplicates, return the summary of its
# ranges.
#
# Example 1:
#
#
# Input:  [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
#
#
# Example 2:
#
#
# Input:  [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
#


class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        L, R = 0, 1
        res = []
        while R < len(nums):
            while R < len(nums) and nums[R] == nums[R-1]+1:
                R += 1
            if L == R-1:
                res.append(str(nums[L]))
            else:
                res.append("{}->{}".format(nums[L], nums[R-1]))
            L, R = R, R+1
        if L != len(nums):
            if L == len(nums)-1:
                res.append(str(nums[-1]))
            else:
                res.append("{}->{}".format(nums[L], nums[-1]))
        return res
