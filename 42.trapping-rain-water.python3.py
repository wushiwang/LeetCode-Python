#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (37.92%)
# Total Accepted:    171.3K
# Total Submissions: 451.5K
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it is able to trap after raining.
#
#
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In
# this case, 6 units of rain water (blue section) are being trapped. Thanks
# Marcos for contributing this image!
#
# Example:
#
#
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
#


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        L, R, cur_low, res = 0, len(height)-1, 0, 0
        while L < R - 1:
            low = min(height[L], height[R])
            if cur_low < low:
                res += (low-cur_low)*(R-L-1)
                cur_low = low
            else:
                if height[L] <= height[R]:
                    L += 1
                    res -= cur_low if cur_low < height[L] else height[L]
                else:
                    R -= 1
                    res -= cur_low if cur_low < height[R] else height[R]
        return res
