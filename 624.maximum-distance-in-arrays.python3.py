#
# [624] Maximum Distance in Arrays
#
# https://leetcode.com/problems/maximum-distance-in-arrays/description/
#
# algorithms
# Easy (35.76%)
# Total Accepted:    11.6K
# Total Submissions: 32.4K
# Testcase Example:  '[[1,2,3],[4,5],[1,2,3]]'
#
#
# Given m arrays, and each array is sorted in ascending order. Now you can pick
# up two integers from two different arrays (each array picks one) and
# calculate the distance. We define the distance between two integers a and b
# to be their absolute difference |a-b|. Your task is to find the maximum
# distance.
#
#
# Example 1:
#
# Input:
# [[1,2,3],
# ⁠[4,5],
# ⁠[1,2,3]]
# Output: 4
# Explanation:
# One way to reach the maximum distance 4 is to pick 1 in the first or third
# array and pick 5 in the second array.
#
#
#
# Note:
#
# Each given array will have at least 1 number. There will be at least two
# non-empty arrays.
# The total number of the integers in all the m arrays will be in the range of
# [2, 10000].
# The integers in the m arrays will be in the range of [-10000, 10000].
#


class Solution:
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        left, right = [], []
        for i in range(len(arrays)):
            if len(arrays[i]) != 0:
                left.append((arrays[i][0], i))
                right.append((arrays[i][-1], i))
        left, right = sorted(left), sorted(right)
        if left[0][1] != right[-1][1]:
            return int(abs(left[0][0] - right[-1][0]))
        else:
            return max(int(abs(left[1][0] - right[-1][0])),\
                       int(abs(left[0][0] - right[-2][0])))
