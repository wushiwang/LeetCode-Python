#
# [711] Number of Distinct Islands II
#
# https://leetcode.com/problems/number-of-distinct-islands-ii/description/
#
# algorithms
# Hard (42.55%)
# Total Accepted:    2.2K
# Total Submissions: 5.3K
# Testcase Example:  '[[1,1,0,0,0],[1,0,0,0,0],[0,0,0,0,1],[0,0,0,1,1]]'
#
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.)  You
# may assume all four edges of the grid are surrounded by water.
#
# Count the number of distinct islands.  An island is considered to be the same
# as another if they have the same shape, or have the same shape after rotation
# (90, 180, or 270 degrees only) or reflection (left/right direction or up/down
# direction).
#
# Example 1:
#
# 11000
# 10000
# 00001
# 00011
#
# Given the above grid map, return 1.
#
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
# are considered same island shapes. Because if we make a 180 degrees clockwise
# rotation on the first island, then two islands will have the same shapes.
#
#
# Example 2:
#
# 11100
# 10001
# 01001
# 01110
# Given the above grid map, return 2.
#
# Here are the two distinct islands:
#
# 111
# 1
#
# and
#
# 1
# 1
#
#
# Notice that:
#
# 111
# 1
#
# and
#
# 1
# 111
#
# are considered same island shapes. Because if we flip the first array in the
# up/down direction, then they have the same shapes.
#
#
# Note:
# The length of each dimension in the given grid does not exceed 50.
#
import collections


class Solution:
    def numDistinctIslands2(self, grid):
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
                    cur = []
                    while len(que) != 0:
                        x, y = que.popleft()
                        cur.append((x, y))
                        for d in range(4):
                            nx, ny = x+dx[d], y+dy[d]
                            if nx+i >= 0 and nx+i < len(grid) and ny+j >= 0 and ny+j < len(grid[0]):
                                if grid[nx+i][ny+j] == 1:
                                    grid[nx+i][ny+j] = 0
                                    que.append((nx, ny))
                    res.add(self.norm(cur))
        return len(res)

    def norm(self, cur):
        lst = [None]*8
        lst[0] = sorted([[x, y] for x, y in cur])
        lst[1] = sorted([[-x, y] for x, y in cur])
        lst[2] = sorted([[x, -y] for x, y in cur])
        lst[3] = sorted([[-x, -y] for x, y in cur])
        lst[4] = sorted([[y, x] for x, y in cur])
        lst[5] = sorted([[-y, x] for x, y in cur])
        lst[6] = sorted([[y, -x] for x, y in cur])
        lst[7] = sorted([[-y, -x] for x, y in cur])
        for i in range(8):
            a, b = lst[i][0][0], lst[i][0][1]
            lst[i] = tuple((x-a, y-b) for x, y in lst[i])
        return sorted(lst)[0]
