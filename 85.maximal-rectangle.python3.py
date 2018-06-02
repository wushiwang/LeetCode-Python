#
# [85] Maximal Rectangle
#
# https://leetcode.com/problems/maximal-rectangle/description/
#
# algorithms
# Hard (29.93%)
# Total Accepted:    88K
# Total Submissions: 293.9K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle
# containing only 1's and return its area.
#
# Example:
#
#
# Input:
# [
# ⁠ ["1","0","1","0","0"],
# ⁠ ["1","0","1","1","1"],
# ⁠ ["1","1","1","1","1"],
# ⁠ ["1","0","0","1","0"]
# ]
# Output: 6
#


class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        res = 0
        dp = [[int(matrix[0][x]) for x in range(0, len(matrix[0]))] for y in range(2)]
        for i in range(1, len(matrix)):
            flag = False
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == "0" and matrix[i-1][j] == "1":
                    if not flag:
                        res = max(res, self.getMaxRectInHistogram(dp[(i+1)&1]))
                        flag = True
                    dp[i&1][j] = 0
                else:
                    dp[i&1][j] = dp[(i+1)&1][j] + int(matrix[i][j])
        res = max(res, self.getMaxRectInHistogram(dp[(len(matrix)-1)&1]))
        return res

    def getMaxRectInHistogram(self, heights):
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
