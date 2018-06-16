#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (37.08%)
# Total Accepted:    185.2K
# Total Submissions: 498.9K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
#
# Example 1:
#
#
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1
#
#
# Example 2:
#
#
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3
#
import collections


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        dx = [1,0,0,-1]
        dy = [0,1,-1,0]
        res = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] == '1':
                    # BFS
                    que = collections.deque()
                    que.append((i, j))
                    visited.add((i, j))
                    while len(que) != 0:
                        x, y = que.popleft()
                        for d in range(4):
                            nx, ny = x+dx[d], y+dy[d]
                            if nx >= 0 and nx < len(grid) and ny >= 0 and ny < len(grid[0]):
                                if (nx, ny) not in visited and grid[nx][ny] == '1':
                                    que.append((nx, ny))
                                    visited.add((nx, ny))
                    res += 1
        return res
