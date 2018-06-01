#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (28.33%)
# Total Accepted:    182.1K
# Total Submissions: 642.7K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where
# "adjacent" cells are those horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
#
# Example:
#
#
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
#


class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if len(board) == 0:
            return False
        self.dx = [0, 1, -1, 0]
        self.dy = [1, 0, 0, -1]
        visited = [[False for x in range(len(board[0]))] for y in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                visited[i][j] = True
                if self.DFS(0, board, word, i, j, visited):
                    return True
                visited[i][j] = False
        return False

    def DFS(self, level, board, word, x, y, visited):
        if board[x][y] == word[level]:
            if level == len(word) - 1:
                return True
            for i in range(4):
                nx, ny = x + self.dx[i], y + self.dy[i]
                if nx >= 0 and nx < len(board) and\
                        ny >= 0 and ny < len(board[0]) and\
                        not visited[nx][ny]:
                    visited[nx][ny] = True
                    if self.DFS(level+1, board, word, nx, ny, visited):
                        return True
                    visited[nx][ny] = False
        return False
