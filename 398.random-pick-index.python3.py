#
# [398] Random Pick Index
#
# https://leetcode.com/problems/random-pick-index/description/
#
# algorithms
# Medium (44.80%)
# Total Accepted:    37.3K
# Total Submissions: 83.2K
# Testcase Example:  '["Solution","pick"]\n[[[1,2,3,3,3]],[3]]'
#
# Given an array of integers with possible duplicates, randomly output the
# index of a given target number. You can assume that the given target number
# must exist in the array.
#
# Note:
# The array size can be very large. Solution that uses too much extra space
# will not pass the judge.
#
# Example:
#
#
# int[] nums = new int[] {1,2,3,3,3};
# Solution solution = new Solution(nums);
#
# // pick(3) should return either index 2, 3, or 4 randomly. Each index should
# have equal probability of returning.
# solution.pick(3);
#
# // pick(1) should return 0. Since in the array only nums[0] is equal to 1.
# solution.pick(1);
#
import random


class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        pos, t = None, 0
        for i in range(len(self.nums)):
            if self.nums[i] == target:
                if random.randint(0, t) == 0:
                    pos = i
                t += 1
        return pos


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
