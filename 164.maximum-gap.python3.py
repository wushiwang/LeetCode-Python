#
# [164] Maximum Gap
#
# https://leetcode.com/problems/maximum-gap/description/
#
# algorithms
# Hard (30.32%)
# Total Accepted:    57.2K
# Total Submissions: 188.7K
# Testcase Example:  '[3,6,9,1]'
#
# Given an unsorted array, find the maximum difference between the successive
# elements in its sorted form.
#
# Return 0 if the array contains less than 2 elements.
#
# Example 1:
#
#
# Input: [3,6,9,1]
# Output: 3
# Explanation: The sorted form of the array is [1,3,6,9], either
# (3,6) or (6,9) has the maximum difference 3.
#
# Example 2:
#
#
# Input: [10]
# Output: 0
# Explanation: The array contains less than 2 elements, therefore return 0.
#
# Note:
#
#
# You may assume all elements in the array are non-negative integers and fit in
# the 32-bit signed integer range.
# Try to solve it in linear time/space.
#


class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        # Get maximum num's digits (10-based)
        MAX = max(nums)
        MAX_D = 0
        while MAX != 0:
            MAX = MAX // 10
            MAX_D += 1
        # Start Radix Sort O(r(10+N)), r in range[1, 32]
        bucket, base = [[] for x in range(10)], 1
        for _ in range(MAX_D):
            for n in nums:
                bucket[(n//base)%10].append(n)
            i = 0
            for b in bucket:
                nums[i:i+len(b)] = b
                i += len(b)
                b.clear()
            base *= 10
        # Get Maximum Gap
        res = 0
        for i in range(1, len(nums)):
            res = max(res, nums[i]-nums[i-1])
        return res
