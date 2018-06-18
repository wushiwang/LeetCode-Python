#
# [220] Contains Duplicate III
#
# https://leetcode.com/problems/contains-duplicate-iii/description/
#
# algorithms
# Medium (18.76%)
# Total Accepted:    70K
# Total Submissions: 373.3K
# Testcase Example:  '[1,2,3,1]\n3\n0'
#
# Given an array of integers, find out whether there are two distinct indices i
# and j in the array such that the absolute difference between nums[i] and
# nums[j] is at most t and the absolute difference between i and j is at most
# k.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true
#
#
#
# Example 2:
#
#
# Input: nums = [1,0,1,1], k = 1, t = 2
# Output: true
#
#
#
# Example 3:
#
#
# Input: nums = [1,5,9,1,5,9], k = 2, t = 3
# Output: false
#


class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k <= 0 or t < 0:
            return False
        dic = dict()
        for i in range(len(nums)):
            pos = nums[i]//(t+1)
            for j in range(pos-1, pos+2):
                if j in dic and abs(dic[j] - nums[i]) <= t:
                    return True
            dic[pos] = nums[i]
            if i >= k:
                dic.pop(nums[i-k]//(t+1))
        return False
