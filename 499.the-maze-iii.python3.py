#
# [499] The Maze III
#
# https://leetcode.com/problems/the-maze-iii/description/
#
# algorithms
# Hard (34.29%)
# Total Accepted:    6K
# Total Submissions: 17.5K
# Testcase Example:  '[[0,0,0,0,0],[1,1,0,0,1],[0,0,0,0,0],[0,1,0,0,1],[0,1,0,0,0]]\n[4,3]\n[0,1]'
#
# There is a ball in a maze with empty spaces and walls. The ball can go
# through empty spaces by rolling up (u), down (d), left (l) or right (r), but
# it won't stop rolling until hitting a wall. When the ball stops, it could
# choose the next direction. There is also a hole in this maze. The ball will
# drop into the hole if it rolls on to the hole.
#
# ⁠Given the ball position, the hole position and the maze, find out how the
# ball could drop into the hole by moving the shortest distance. The distance
# is defined by the number of empty spaces traveled by the ball from the start
# position (excluded) to the hole (included). Output the moving directions by
# using 'u', 'd', 'l' and 'r'. Since there could be several different shortest
# ways, you should output the lexicographically smallest way. If the ball
# cannot reach the hole, output "impossible".
#
# The maze is represented by a binary 2D array. 1 means the wall and 0 means
# the empty space. You may assume that the borders of the maze are all walls.
# The ball and the hole coordinates are represented by row and column
# indexes.
#
#
# Example 1
#
# Input 1: a maze represented by a 2D array
#
# 0 0 0 0 0
# 1 1 0 0 1
# 0 0 0 0 0
# 0 1 0 0 1
# 0 1 0 0 0
#
# Input 2: ball coordinate (rowBall, colBall) = (4, 3)
# Input 3: hole coordinate (rowHole, colHole) = (0, 1)
#
# Output: "lul"
# Explanation: There are two shortest ways for the ball to drop into the hole.
# The first way is left -> up -> left, represented by "lul".
# The second way is up -> left, represented by 'ul'.
# Both ways have shortest distance 6, but the first way is lexicographically
# smaller because 'l' < 'u'. So the output is "lul".
#
#
#
#
#
# Example 2
#
# Input 1: a maze represented by a 2D array
#
# 0 0 0 0 0
# 1 1 0 0 1
# 0 0 0 0 0
# 0 1 0 0 1
# 0 1 0 0 0
#
# Input 2: ball coordinate (rowBall, colBall) = (4, 3)
# Input 3: hole coordinate (rowHole, colHole) = (3, 0)
# Output: "impossible"
# Explanation: The ball cannot reach the hole.
#
#
#
#
# Note:
#
# There is only one ball and one hole in the maze.
# Both the ball and hole exist on an empty space, and they will not be at the
# same position initially.
# The given maze does not contain border (like the red rectangle in the example
# pictures), but you could assume the border of the maze are all walls.
# The maze contains at least 2 empty spaces, and the width and the height of
# the maze won't exceed 30.
#
import math


class Solution:
    def findShortestWay(self, maze, ball, hole):
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str
        """
        self.dx = [1, 0, 0, -1]
        self.dy = [0, -1, 1, 0]
        self.name = ['d', 'l', 'r', 'u']
        self.l = math.inf
        self.res = ''
        self.dis = [[math.inf for x in range(len(maze[0]))] for y in range(len(maze))]
        self.dis[ball[0]][ball[1]] = 0
        self.DFS(maze, ball[0], ball[1], hole[0], hole[1], 0, '', -1)
        if self.l == math.inf:
            return "impossible"
        else:
            return self.res

    def DFS(self, maze, x, y, hx, hy, l, cur, od):
        if l > self.l or l > self.dis[x][y]:
            return
        for d in range(4):
            if d != od or not ((od == 0 and d == 3) or (od == 1 and d == 2) or (od == 2 and d == 1) or (od == 3 and d == 0)):
                nx, ny, ncur, nl = x, y, cur+self.name[d], l
                while True:
                    if nx+self.dx[d] >= 0 and nx+self.dx[d] < len(maze) and\
                            ny+self.dy[d] >= 0 and ny+self.dy[d] < len(maze[0]) and\
                            maze[nx+self.dx[d]][ny+self.dy[d]] == 0:
                        nx, ny, nl = nx+self.dx[d], ny+self.dy[d], nl+1
                        if nx == hx and ny == hy and nl < self.l:
                            self.l, self.res = nl, ncur
                    else:
                        break
                if not (nx == x and ny == y):
                    self.dis[nx][ny] = min(self.dis[nx][ny], nl)
                    self.DFS(maze, nx, ny, hx, hy, nl, ncur, d)
