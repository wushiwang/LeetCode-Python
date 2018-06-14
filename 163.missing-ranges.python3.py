#
# [163] Missing Ranges
#
# https://leetcode.com/problems/missing-ranges/description/
#
# algorithms
# Medium (23.03%)
# Total Accepted:    40.5K
# Total Submissions: 175.8K
# Testcase Example:  '[0,1,3,50,75]\n0\n99'
#
# Given a sorted integer array nums, where the range of elements are in the
# inclusive range [lower, upper], return its missing ranges.
#
# Example:
#
#
# Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
# Output: ["2", "4->49", "51->74", "76->99"]
#


class Solution:
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        res = []
        if len(nums) == 0:
            self.add_res(res, lower, upper)
            return res
        if nums[0] != lower:
            self.add_res(res, lower, nums[0]-1)
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]+1:
                self.add_res(res, nums[i-1]+1, nums[i]-1)
        if nums[-1] != upper:
            self.add_res(res, nums[-1]+1, upper)
        return res

    def add_res(self, res, a, b):
        if a == b:
            res.append(str(a))
        else:
            res.append(str(a)+"->"+str(b))
