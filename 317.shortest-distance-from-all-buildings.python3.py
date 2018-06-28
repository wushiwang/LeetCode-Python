#
# [317] Shortest Distance from All Buildings
#
# https://leetcode.com/problems/shortest-distance-from-all-buildings/description/
#
# algorithms
# Hard (34.89%)
# Total Accepted:    25.3K
# Total Submissions: 72.6K
# Testcase Example:  '[[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]'
#
# You want to build a house on an empty land which reaches all buildings in the
# shortest amount of distance. You can only move up, down, left and right. You
# are given a 2D grid of values 0, 1 or 2, where:
#
#
# Each 0 marks an empty land which you can pass by freely.
# Each 1 marks a building which you cannot pass through.
# Each 2 marks an obstacle which you cannot pass through.
#
#
# Example:
#
#
# Input: [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
#
# 1 - 0 - 2 - 0 - 1
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 1 - 0 - 0
#
# Output: 7
#
# Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at
# (0,2),
# ⁠            the point (1,2) is an ideal empty land to build a house, as the
# total
# travel distance of 3+3+1=7 is minimal. So return 7.
#
# Note:
# There will be at least one building. If it is not possible to build such
# house according to the above rules, return -1.
#
import collections
import math


class Solution:
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid) == 0:
            return -1
        dx = [1,0,0,-1]
        dy = [0,1,-1,0]
        dis = [[[0, 0] for x in range(len(grid[0]))] for y in range(len(grid))]
        ones = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ones += 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # BFS
                    que, cnt, visited = collections.deque(), 1, set()
                    que.append((i, j, 0))
                    visited.add((i, j))
                    while len(que) != 0:
                        x, y, v = que.popleft()
                        dis[x][y][0] += v
                        dis[x][y][1] += 1
                        for d in range(4):
                            nx, ny = x+dx[d], y+dy[d]
                            if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]):
                                if (nx, ny) not in visited:
                                    if grid[nx][ny] == 0:
                                        visited.add((nx, ny))
                                        que.append((nx, ny, v+1))
                                    elif grid[nx][ny] == 1 and grid[x][y] != 1:
                                        visited.add((nx, ny))
                                        cnt += 1
                    if cnt != ones:
                        return -1
        res = math.inf
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and dis[i][j][1] == ones:
                    res = min(res, dis[i][j][0])
        return res if res != math.inf else -1
