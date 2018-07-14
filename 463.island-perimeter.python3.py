#
# [463] Island Perimeter
#
# https://leetcode.com/problems/island-perimeter/description/
#
# algorithms
# Easy (58.25%)
# Total Accepted:    88.6K
# Total Submissions: 152.1K
# Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
#
# You are given a map in form of a two-dimensional integer grid where 1
# represents land and 0 represents water. Grid cells are connected
# horizontally/vertically (not diagonally). The grid is completely surrounded
# by water, and there is exactly one island (i.e., one or more connected land
# cells). The island doesn't have "lakes" (water inside that isn't connected to
# the water around the island). One cell is a square with side length 1. The
# grid is rectangular, width and height don't exceed 100. Determine the
# perimeter of the island.
#
# Example:
#
# [[0,1,0,0],
# ⁠[1,1,1,0],
# ⁠[0,1,0,0],
# ⁠[1,1,0,0]]
#
# Answer: 16
# Explanation: The perimeter is the 16 yellow stripes in the image below:
#
#


class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        dx = [0, 1, -1, 0]
        dy = [1, 0, 0, -1]
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    for d in range(4):
                        nx, ny = i+dx[d], j+dy[d]
                        if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]):
                            if grid[nx][ny] == 0:
                                res += 1
                        else:
                            res += 1
        return res
