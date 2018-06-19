#
# [229] Majority Element II
#
# https://leetcode.com/problems/majority-element-ii/description/
#
# algorithms
# Medium (29.49%)
# Total Accepted:    73.6K
# Total Submissions: 249.3K
# Testcase Example:  '[3,2,3]'
#
# Given an integer array of size n, find all elements that appear more than ⌊
# n/3 ⌋ times.
#
# Note: The algorithm should run in linear time and in O(1) space.
#
# Example 1:
#
#
# Input: [3,2,3]
# Output: [3]
#
# Example 2:
#
#
# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]
#


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Boyer-Moore Majority Vote Algorithm
        if len(nums) <= 1:
            return nums
        num1, num2, cnt1, cnt2 = None, None, 0, 0
        for n in nums:
            if num1 == n:
                cnt1 += 1
            elif num2 == n:
                cnt2 += 1
            elif cnt1 == 0:
                num1, cnt1 = n, 1
            elif cnt2 == 0:
                num2, cnt2 = n, 1
            else:
                cnt1, cnt2 = cnt1-1, cnt2-1
        # Check result
        cnt1, cnt2 = 0, 0
        for n in nums:
            if n == num1:
                cnt1 += 1
            elif n == num2:
                cnt2 += 1
        res = []
        if cnt1 > len(nums) // 3:
            res.append(num1)
        if cnt2 > len(nums) // 3:
            res.append(num2)
        return res
