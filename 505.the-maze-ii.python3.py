#
# [505] The Maze II
#
# https://leetcode.com/problems/the-maze-ii/description/
#
# algorithms
# Medium (38.89%)
# Total Accepted:    13.9K
# Total Submissions: 35.7K
# Testcase Example:  '[[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]\n[0,4]\n[4,4]'
#
# There is a ball in a maze with empty spaces and walls. The ball can go
# through empty spaces by rolling up, down, left or right, but it won't stop
# rolling until hitting a wall. When the ball stops, it could choose the next
# direction.
#
# Given the ball's start position, the destination and the maze, find the
# shortest distance for the ball to stop at the destination. The distance is
# defined by the number of empty spaces traveled by the ball from the start
# position (excluded) to the destination (included). If the ball cannot stop at
# the destination, return -1.
#
# The maze is represented by a binary 2D array. 1 means the wall and 0 means
# the empty space. You may assume that the borders of the maze are all walls.
# The start and destination coordinates are represented by row and column
# indexes.
#
#
# Example 1
#
# Input 1: a maze represented by a 2D array
#
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
#
# Input 2: start coordinate (rowStart, colStart) = (0, 4)
# Input 3: destination coordinate (rowDest, colDest) = (4, 4)
#
# Output: 12
# Explanation: One shortest way is : left -> down -> left -> down -> right ->
# down -> right.
# ⁠            The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.
#
#
#
#
#
# Example 2
#
# Input 1: a maze represented by a 2D array
#
# 0 0 1 0 0
# 0 0 0 0 0
# 0 0 0 1 0
# 1 1 0 1 1
# 0 0 0 0 0
#
# Input 2: start coordinate (rowStart, colStart) = (0, 4)
# Input 3: destination coordinate (rowDest, colDest) = (3, 2)
#
# Output: -1
# Explanation: There is no way for the ball to stop at the destination.
#
#
#
#
# Note:
#
# There is only one ball and one destination in the maze.
# Both the ball and the destination exist on an empty space, and they will not
# be at the same position initially.
# The given maze does not contain border (like the red rectangle in the example
# pictures), but you could assume the border of the maze are all walls.
# The maze contains at least 2 empty spaces, and both the width and height of
# the maze won't exceed 100.
#
import math
import heapq


class Solution:
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        dx = [0, 1, -1, 0]
        dy = [1, 0, 0, -1]
        dis = [[math.inf for x in range(len(maze[0]))] for y in range(len(maze))]
        dis[start[0]][start[1]] = 0
        heap = []
        heap.append((0, start[0], start[1]))
        while len(heap) != 0:
            cur, x, y = heapq.heappop(heap)
            for d in range(4):
                nx, ny, ncur = x, y, cur
                nnx, nny = nx+dx[d], ny+dy[d]
                while nnx >= 0 and nnx < len(maze) and\
                        nny >= 0 and nny < len(maze[0]) and\
                        maze[nnx][nny] == 0:
                    nx, ny, ncur = nnx, nny, ncur+1
                    nnx, nny = nnx+dx[d], nny+dy[d]
                if ncur < dis[nx][ny]:
                    if nx == destination[0] and ny == destination[1]:
                        return ncur
                    dis[nx][ny] = ncur
                    heapq.heappush(heap, (ncur, nx, ny))
        return -1
