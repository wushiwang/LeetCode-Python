#
# [490] The Maze
#
# https://leetcode.com/problems/the-maze/description/
#
# algorithms
# Medium (43.75%)
# Total Accepted:    16.2K
# Total Submissions: 37K
# Testcase Example:  '[[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]]\n[0,4]\n[4,4]'
#
# There is a ball in a maze with empty spaces and walls. The ball can go
# through empty spaces by rolling up, down, left or right, but it won't stop
# rolling until hitting a wall. When the ball stops, it could choose the next
# direction.
#
# Given the ball's start position, the destination and the maze, determine
# whether the ball could stop at the destination.
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
# Output: true
# Explanation: One possible way is : left -> down -> left -> down -> right ->
# down -> right.
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
# Output: false
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


class Solution:
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        self.dx = [1,0,0,-1]
        self.dy = [0,1,-1,0]
        check = False
        for d in range(4):
            nx, ny = destination[0]+self.dx[d], destination[1]+self.dy[d]
            if nx < 0 or nx > len(maze) or ny < 0 or ny < len(maze[0]) or maze[nx][ny] == 1:
                check = True
                break
        if not check:
            return False
        visited = set()
        visited.add((start[0], start[1]))
        return self.DFS(maze, start[0], start[1], visited, destination[0], destination[1])

    def DFS(self, maze, x, y, visited, desx, desy):
        if x == desx and y == desy:
            return True
        for d in range(4):
            nx, ny = x, y
            while True:
                if nx+self.dx[d] >= 0 and nx+self.dx[d] < len(maze) and\
                        ny+self.dy[d] >= 0 and ny+self.dy[d] < len(maze[0]) and\
                        maze[nx+self.dx[d]][ny+self.dy[d]] == 0:
                        nx, ny = nx+self.dx[d], ny+self.dy[d]
                else:
                    break
            if (nx, ny) not in visited:
                visited.add((nx, ny))
                if self.DFS(maze, nx, ny, visited, desx, desy):
                    return True
        return False
