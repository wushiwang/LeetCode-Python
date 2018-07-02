#
# [361] Bomb Enemy
#
# https://leetcode.com/problems/bomb-enemy/description/
#
# algorithms
# Medium (40.68%)
# Total Accepted:    25.2K
# Total Submissions: 61.9K
# Testcase Example:  '[["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]'
#
# Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0'
# (the number zero), return the maximum enemies you can kill using one bomb.
# The bomb kills all the enemies in the same row and column from the planted
# point until it hits the wall since the wall is too strong to be destroyed.
# ⁠Note that you can only put the bomb at an empty cell.
#
# Example:
#
# For the given grid
#
# 0 E 0 0
# E 0 W E
# 0 E 0 0
#
# return 3. (Placing a bomb at (1,1) kills 3 enemies)
#
#
#
# Credits:Special thanks to @memoryless for adding this problem and creating
# all test cases.
#


class Solution:
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        lr = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]
        rl = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]
        ud = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]
        du = [[0 for x in range(len(grid[0]))] for y in range(len(grid))]

        for i in range(len(grid)):
            cur = 0
            for j in range(len(grid[0])):
                if grid[i][j] == 'E':
                    cur += 1
                elif grid[i][j] == 'W':
                    cur = 0
                else:
                    lr[i][j] = cur
        for i in range(len(grid)):
            cur = 0
            for j in range(len(grid[0])-1, -1, -1):
                if grid[i][j] == 'E':
                    cur += 1
                elif grid[i][j] == 'W':
                    cur = 0
                else:
                    rl[i][j] = cur
        for j in range(len(grid[0])):
            cur = 0
            for i in range(len(grid)):
                if grid[i][j] == 'E':
                    cur += 1
                elif grid[i][j] == 'W':
                    cur = 0
                else:
                    ud[i][j] = cur
        for j in range(len(grid[0])):
            cur = 0
            for i in range(len(grid)-1, -1, -1):
                if grid[i][j] == 'E':
                    cur += 1
                elif grid[i][j] == 'W':
                    cur = 0
                else:
                    du[i][j] = cur
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    res = max(res, lr[i][j]+rl[i][j]+ud[i][j]+du[i][j])
        return res
