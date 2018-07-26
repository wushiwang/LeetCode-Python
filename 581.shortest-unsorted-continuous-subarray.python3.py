#
# [581] Shortest Unsorted Continuous Subarray
#
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/
#
# algorithms
# Easy (29.37%)
# Total Accepted:    40.8K
# Total Submissions: 138.8K
# Testcase Example:  '[2,6,4,8,10,9,15]'
#
# Given an integer array, you need to find one continuous subarray that if you
# only sort this subarray in ascending order, then the whole array will be
# sorted in ascending order, too.
#
# You need to find the shortest such subarray and output its length.
#
# Example 1:
#
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the
# whole array sorted in ascending order.
#
#
#
# Note:
#
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means .
#


class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        biggest = [nums[0]]
        cur_biggest = nums[0]
        for n in nums[1:]:
            if n >= cur_biggest:
                cur_biggest = n
            biggest.append(cur_biggest)
        R = len(nums)-1
        for i in range(len(biggest)-1, -1, -1):
            if nums[i] == biggest[i]:
                R -= 1
            else:
                break
        R += 1
        smallest = [nums[-1]]
        cur_smallest = nums[-1]
        for n in nums[:-1][::-1]:
            if n <= cur_smallest:
                cur_smallest = n
            smallest.append(cur_smallest)
        smallest = smallest[::-1]
        L = 0
        for i in range(len(biggest)):
            if nums[i] == smallest[i]:
                L += 1
            else:
                break
        L -= 1
        if L == len(nums)-1:
            return 0
        return R - L - 1
