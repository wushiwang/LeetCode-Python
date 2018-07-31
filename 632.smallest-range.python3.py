#
# [632] Smallest Range
#
# https://leetcode.com/problems/smallest-range/description/
#
# algorithms
# Hard (42.82%)
# Total Accepted:    12.1K
# Total Submissions: 28.2K
# Testcase Example:  '[[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]'
#
# You have k lists of sorted integers in ascending order. Find the smallest
# range that includes at least one number from each of the k lists.
#
# We define the range [a,b] is smaller than range [c,d] if b-a < d-c or a < c
# if b-a == d-c.
#
# Example 1:
#
# Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
# Output: [20,24]
# Explanation:
# List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
# List 2: [0, 9, 12, 20], 20 is in range [20,24].
# List 3: [5, 18, 22, 30], 22 is in range [20,24].
#
#
#
#
# Note:
#
# The given list may contain duplicates, so ascending order means >= here.
# 1 k
# ⁠-105 value of elements 5.
# For Java users, please note that the input type has been changed to
# List<List<Integer>>. And after you reset the code template, you'll see this
# point.
#
#


class Solution:
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        lst = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                lst.append((nums[i][j], i))
        lst = sorted(lst, key=lambda x: x[0])
        if len(nums) == 1:
            return [lst[0][0], lst[0][0]]
        L, R, cur, dic = 0, 0, 0, dict()
        res_L, res_R = lst[0][0], lst[-1][0]
        while R < len(lst):
            if lst[R][1] not in dic:
                dic[lst[R][1]] = 0
                cur += 1
            dic[lst[R][1]] += 1
            while cur == len(nums):
                if lst[R][0] - lst[L][0] < res_R - res_L:
                    res_L, res_R = lst[L][0], lst[R][0]
                elif lst[R][0] - lst[L][0] == res_R - res_L:
                    if lst[L][0] < res_L:
                        res_L, res_R = lst[L][0], lst[R][0]
                dic[lst[L][1]] -= 1
                if dic[lst[L][1]] == 0:
                    dic.pop(lst[L][1])
                    cur -= 1
                L += 1
            R += 1
        return [res_L, res_R]
