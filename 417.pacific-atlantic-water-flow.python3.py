#
# [417] Pacific Atlantic Water Flow
#
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
#
# algorithms
# Medium (35.08%)
# Total Accepted:    28.4K
# Total Submissions: 80.8K
# Testcase Example:  '[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]'
#
# Given an m x n matrix of non-negative integers representing the height of
# each unit cell in a continent, the "Pacific ocean" touches the left and top
# edges of the matrix and the "Atlantic ocean" touches the right and bottom
# edges.
#
# Water can only flow in four directions (up, down, left, or right) from a cell
# to another one with height equal or lower.
#
# Find the list of grid coordinates where water can flow to both the Pacific
# and Atlantic ocean.
#
# Note:
#
# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
#
#
# Example:
#
# Given the following 5x5 matrix:
#
# ⁠ Pacific ~   ~   ~   ~   ~
# ⁠      ~  1   2   2   3  (5) *
# ⁠      ~  3   2   3  (4) (4) *
# ⁠      ~  2   4  (5)  3   1  *
# ⁠      ~ (6) (7)  1   4   5  *
# ⁠      ~ (5)  1   1   2   4  *
# ⁠         *   *   *   *   * Atlantic
#
# Return:
#
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with
# parentheses in above matrix).
#
import collections


class Solution:
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        # BFS
        if len(matrix) == 0:
            return []
        dx = [0, 1, -1, 0]
        dy = [1, 0, 0, -1]
        mark = [[0 for x in range(len(matrix[0]))] for y in range(len(matrix))]
        # 1. mark all nodes can reach Pacific
        que, visited = collections.deque(), set()
        for j in range(len(matrix[0])):
            que.append((0, j))
            visited.add((0, j))
        for i in range(1, len(matrix)):
            que.append((i, 0))
            visited.add((i, 0))
        while len(que) != 0:
            x, y = que.popleft()
            mark[x][y] += 1
            for d in range(4):
                nx, ny = x+dx[d], y+dy[d]
                if nx >= 0 and nx < len(matrix) and ny >= 0 and ny < len(matrix[0]):
                    if (nx, ny) not in visited and matrix[nx][ny] >= matrix[x][y]:
                        visited.add((nx, ny))
                        que.append((nx, ny))
        # 2. mark all nodes can reach Atlantic
        que, visited = collections.deque(), set()
        for j in range(len(matrix[0])):
            que.append((len(matrix)-1, j))
            visited.add((len(matrix)-1, j))
        for i in range(len(matrix)-1):
            que.append((i, len(matrix[0])-1))
            visited.add((i, len(matrix[0])-1))
        while len(que) != 0:
            x, y = que.popleft()
            mark[x][y] += 1
            for d in range(4):
                nx, ny = x+dx[d], y+dy[d]
                if nx >= 0 and nx < len(matrix) and ny >= 0 and ny < len(matrix[0]):
                    if (nx, ny) not in visited and matrix[nx][ny] >= matrix[x][y]:
                        visited.add((nx, ny))
                        que.append((nx, ny))
        # 3. get result
        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if mark[i][j] == 2:
                    res.append([i, j])
        return res
