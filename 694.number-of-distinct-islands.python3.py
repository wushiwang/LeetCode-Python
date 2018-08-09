#
# [694] Number of Distinct Islands
#
# https://leetcode.com/problems/number-of-distinct-islands/description/
#
# algorithms
# Medium (45.60%)
# Total Accepted:    9.9K
# Total Submissions: 21.7K
# Testcase Example:  '[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]'
#
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.)  You
# may assume all four edges of the grid are surrounded by water.
#
# Count the number of distinct islands.  An island is considered to be the same
# as another if and only if one island can be translated (and not rotated or
# reflected) to equal the other.
#
# Example 1:
#
# 11000
# 11000
# 00011
# 00011
#
# Given the above grid map, return 1.
#
#
# Example 2:
# 11011
# 10000
# 00001
# 11011
# Given the above grid map, return 3.
# Notice that:
#
# 11
# 1
#
# and
#
# ⁠1
# 11
#
# are considered different island shapes, because we do not consider reflection
# / rotation.
#
#
# Note:
# The length of each dimension in the given grid does not exceed 50.
#
import collections


class Solution:
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        dx = [0, 1, -1, 0]
        dy = [1, 0, 0, -1]
        res = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    que = collections.deque()
                    que.append((0, 0))
                    visited = [(0, 0)]
                    while len(que) != 0:
                        x, y = que.popleft()
                        for d in range(4):
                            nx, ny = dx[d]+x, dy[d]+y
                            if nx+i >= 0 and nx+i < len(grid) and ny+j >= 0 and ny+j < len(grid[0]):
                                if grid[nx+i][ny+j] == 1:
                                    grid[nx+i][ny+j] = 0
                                    visited.append((nx, ny))
                                    que.append((nx, ny))
                    res.add(tuple(visited))
        return len(res)
