#
# [286] Walls and Gates
#
# https://leetcode.com/problems/walls-and-gates/description/
#
# algorithms
# Medium (45.78%)
# Total Accepted:    48.8K
# Total Submissions: 106.7K
# Testcase Example:  '[[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]'
#
# You are given a m x n 2D grid initialized with these three possible
# values.
#
#
# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to
# represent INF as you may assume that the distance to a gate is less than
# 2147483647.
#
#
# Fill each empty room with the distance to its nearest gate. If it is
# impossible to reach a gate, it should be filled with INF.
#
# Example: 
#
# Given the 2D grid:
#
#
# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
# ⁠ 0  -1 INF INF
#
#
# After running your function, the 2D grid should be:
#
#
# ⁠ 3  -1   0   1
# ⁠ 2   2   1  -1
# ⁠ 1  -1   2  -1
# ⁠ 0  -1   3   4
#
import collections


class Solution:
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if len(rooms) == 0:
            return
        # Multi-source BFS
        dx = [0, 1, -1, 0]
        dy = [1, 0, 0, -1]
        INF = 2**31 - 1

        que = collections.deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    que.append((i, j, 0))
        while len(que) != 0:
            x, y, l = que.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if nx >= 0 and nx < len(rooms) and ny >= 0 and ny < len(rooms[0]):
                    if rooms[nx][ny] == INF:
                        rooms[nx][ny] = l+1
                        que.append((nx, ny, l+1))
        return
