#
# [37] Sudoku Solver
#
# https://leetcode.com/problems/sudoku-solver/description/
#
# algorithms
# Hard (32.42%)
# Total Accepted:    93.9K
# Total Submissions: 289.3K
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],
# ["6",".",".","1","9","5",".",".","."],
# [".","9","8",".",".",".",".","6","."],
# ["8",".",".",".","6",".",".",".","3"],
# ["4",".",".","8",".","3",".",".","1"],
# ["7",".",".",".","2",".",".",".","6"],
# [".","6",".",".",".",".","2","8","."],
# [".",".",".","4","1","9",".",".","5"],
# [".",".",".",".","8",".",".","7","9"]]'
#
# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# A sudoku solution must satisfy all of the following rules:
#
#
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the the digits 1-9 must occur exactly once in each of the 9 3x3
# sub-boxes of the grid.
#
#
# Empty cells are indicated by the character '.'.
#
#
# A sudoku puzzle...
#
#
# ...and its solution numbers marked in red.
#
# Note:
#
#
# The given board contain only digits 1-9 and the character '.'.
# You may assume that the given Sudoku puzzle will have a single unique
# solution.
# The given board size is always 9x9.
#


class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.check_row = [[False for x in range(10)] for y in range(9)]
        self.check_col = [[False for x in range(10)] for y in range(9)]
        self.check_box = [[False for x in range(10)] for y in range(9)]
        self.ans = False

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    self.check_row[i][int(board[i][j])] = True
                    self.check_col[j][int(board[i][j])] = True
                    self.check_box[(i//3)*3+j//3][int(board[i][j])] = True

        self.DFS(board, 0, 0)
        return

    def DFS(self, board, m, n):
        if m == 9 and n == 0:
            self.ans = True
            return
        if board[m][n] != '.':
            if n + 1 == 9:
                self.DFS(board, m+1, 0)
            else:
                self.DFS(board, m, n+1)
        else:
            for i in range(1, 10):
                if not (self.check_row[m][i] or\
                        self.check_col[n][i] or\
                        self.check_box[(m//3)*3+n//3][i]):
                    self.check_row[m][i], self.check_col[n][i], self.check_box[(m//3)*3+n//3][i] =\
                        True, True, True
                    board[m][n] = str(i)
                    if n + 1 == 9:
                        self.DFS(board, m+1, 0)
                    else:
                        self.DFS(board, m, n+1)
                    if self.ans:
                        return
                    board[m][n] = '.'
                    self.check_row[m][i], self.check_col[n][i], self.check_box[(m//3)*3+n//3][i] =\
                        False, False, False
