#
# [695] Max Area of Island
#
# https://leetcode.com/problems/max-area-of-island/description/
#
# algorithms
# Easy (52.43%)
# Total Accepted:    37.5K
# Total Submissions: 71.5K
# Testcase Example:  '[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]'
#
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.)  You
# may assume all four edges of the grid are surrounded by water.
#
# Find the maximum area of an island in the given 2D array.
# (If there is no island, the maximum area is 0.)
#
# Example 1:
#
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,1,1,0,1,0,0,0,0,0,0,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,0,1,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,1,1,0,0],
# ⁠[0,0,0,0,0,0,0,0,0,0,1,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,0,0,0,0]]
#
# Given the above grid, return 6.
#
# Note the answer is not 11, because the island must be connected
# 4-directionally.
#
#
# Example 2:
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
#
#
# Note:
# The length of each dimension in the given grid does not exceed 50.
#
import collections


class Solution:
    def maxAreaOfIsland(self, grid):
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
                    grid[i][j] = 0
                    area = 1
                    que = collections.deque()
                    que.append((i, j))
                    while len(que) != 0:
                        x, y = que.popleft()
                        for d in range(4):
                            nx, ny = dx[d]+x, dy[d]+y
                            if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]):
                                if grid[nx][ny] == 1:
                                    grid[nx][ny] = 0
                                    area += 1
                                    que.append((nx, ny))
                    res = max(res, area)
        return res
