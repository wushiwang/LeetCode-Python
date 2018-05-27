#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (37.20%)
# Total Accepted:    203.2K
# Total Submissions: 546.3K
# Testcase Example:  '[1,1]'
#
# Given n non-negative integers a1, a2, ..., an, where each represents a point
# at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
# of line i is at (i, ai) and (i, 0). Find two lines, which together with
# x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.
#


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        L, R, res = 0, len(height)-1, 0
        while L < R:
            res = max(res, (R - L)*min(height[L], height[R]))
            if height[L] < height[R]:
                L = L + 1
            else:
                R = R - 1

        return res
