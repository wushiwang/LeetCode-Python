#
# [329] Longest Increasing Path in a Matrix
#
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
#
# algorithms
# Hard (37.61%)
# Total Accepted:    56K
# Total Submissions: 148.8K
# Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
#
# Given an integer matrix, find the length of the longest increasing path.
#
# From each cell, you can either move to four directions: left, right, up or
# down. You may NOT move diagonally or move outside of the boundary (i.e.
# wrap-around is not allowed).
#
# Example 1:
#
#
# Input: nums =
# [
# ⁠ [9,9,4],
# ⁠ [6,6,8],
# ⁠ [2,1,1]
# ]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].
#
#
# Example 2:
#
#
# Input: nums =
# [
# ⁠ [3,4,5],
# ⁠ [3,2,6],
# ⁠ [2,2,1]
# ]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally
# is not allowed.
#


class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if len(matrix) == 0:
            return 0
        self.dx = [1,0,0,-1]
        self.dy = [0,1,-1,0]
        self.dic = [[0 for x in range(len(matrix[0]))] for y in range(len(matrix))]
        visited = [[False for x in range(len(matrix[0]))] for y in range(len(matrix))]
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                visited[i][j] = True
                res = max(res, self.DFS(i, j, visited, matrix))
                visited[i][j] = False
        return res

    def DFS(self, i, j, visited, matrix):
        if self.dic[i][j] != 0:
            return self.dic[i][j]
        res = 1
        for d in range(4):
            nx, ny = i+self.dx[d], j+self.dy[d]
            if nx >= 0 and nx < len(matrix) and ny >= 0 and ny < len(matrix[0]):
                if matrix[nx][ny] < matrix[i][j] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    res = max(res, self.DFS(nx, ny, visited, matrix)+1)
                    visited[nx][ny] = False
        self.dic[i][j] = res
        return res
