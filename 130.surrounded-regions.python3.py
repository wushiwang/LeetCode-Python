#
# [130] Surrounded Regions
#
# https://leetcode.com/problems/surrounded-regions/description/
#
# algorithms
# Medium (19.93%)
# Total Accepted:    104.6K
# Total Submissions: 524.6K
# Testcase Example:  '[["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]'
#
# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions
# surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded
# region.
#
# Example:
#
#
# X X X X
# X O O X
# X X O X
# X O X X
#
#
# After running your function, the board should be:
#
#
# X X X X
# X X X X
# X X X X
# X O X X
#
#
# Explanation:
#
# Surrounded regions shouldn’t be on the border, which means that any 'O' on
# the border of the board are not flipped to 'X'. Any 'O' that is not on the
# border and it is not connected to an 'O' on the border will be flipped to
# 'X'. Two cells are connected if they are adjacent cells connected
# horizontally or vertically.
#


class Solution:
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        self.dx = [0,1,-1,0]
        self.dy = [1,0,0,-1]
        m, n = len(board), len(board[0])
        for i in range(m):
            self.DFS(i, 0, board, m, n)
            self.DFS(i, n-1, board, m, n)

        for i in range(n):
            self.DFS(0, i, board, m, n)
            self.DFS(m-1, i, board, m, n)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '-':
                    board[i][j] = 'O'
        return

    def DFS(self, x, y, board, m, n):
        if board[x][y] == 'O':
            board[x][y] = '-'
        else:
            return
        for i in range(4):
            nx, ny = x + self.dx[i], y + self.dy[i]
            if nx >= 0 and nx < m and ny >= 0 and ny < n:
                self.DFS(nx, ny, board, m, n)
