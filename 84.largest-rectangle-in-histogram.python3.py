#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (27.84%)
# Total Accepted:    120.7K
# Total Submissions: 433.3K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# Given n non-negative integers representing the histogram's bar height where
# the width of each bar is 1, find the area of largest rectangle in the
# histogram.
#
#
# Above is a histogram where width of each bar is 1, given height =
# [2,1,5,6,2,3].
#
#
#
#
# The largest rectangle is shown in the shaded area, which has area = 10
# unit.
#
#
#
# Example:
#
#
# Input: [2,1,5,6,2,3]
# Output: 10
#


class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        res = 0
        stack = []
        LR, RL = [0 for x in range(len(heights))], [0 for x in range(len(heights))]
        # Left to right
        for i in range(0, len(heights)):
            if not (len(stack) == 0 or heights[i] > heights[stack[-1]]):
                while len(stack) != 0 and heights[stack[-1]] >= heights[i]:
                    LR[i] += LR[stack.pop()] + 1
            stack.append(i)
        stack = []
        # Right to left
        for i in range(len(heights)-1, -1, -1):
            if not (len(stack) == 0 or heights[i] > heights[stack[-1]]):
                while len(stack) != 0 and heights[stack[-1]] >= heights[i]:
                    RL[i] += RL[stack.pop()] + 1
            stack.append(i)
            res = max(res, heights[i]*(1+LR[i]+RL[i]))
        return res
