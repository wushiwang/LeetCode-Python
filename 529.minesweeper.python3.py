#
# [529] Minesweeper
#
# https://leetcode.com/problems/minesweeper/description/
#
# algorithms
# Medium (49.60%)
# Total Accepted:    19.7K
# Total Submissions: 39.7K
# Testcase Example:  '[["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]\n[3,0]'
#
# Let's play the minesweeper game (Wikipedia, online game)!
#
# You are given a 2D char matrix representing the game board. 'M' represents an
# unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a
# revealed blank square that has no adjacent (above, below, left, right, and
# all 4 diagonals) mines, digit ('1' to '8') represents how many mines are
# adjacent to this revealed square, and finally 'X' represents a revealed
# mine.
#
# Now given the next click position (row and column indices) among all the
# unrevealed squares ('M' or 'E'), return the board after revealing this
# position according to the following rules:
#
#
#
# If a mine ('M') is revealed, then the game is over - change it to 'X'.
# If an empty square ('E') with no adjacent mines is revealed, then change it
# to revealed blank ('B') and all of its adjacent unrevealed squares should be
# revealed recursively.
# If an empty square ('E') with at least one adjacent mine is revealed, then
# change it to a digit ('1' to '8') representing the number of adjacent mines.
# Return the board when no more squares will be revealed.
#
#
#
# Example 1:
#
# Input:
#
# [['E', 'E', 'E', 'E', 'E'],
# ⁠['E', 'E', 'M', 'E', 'E'],
# ⁠['E', 'E', 'E', 'E', 'E'],
# ⁠['E', 'E', 'E', 'E', 'E']]
#
# Click : [3,0]
#
# Output:
#
# [['B', '1', 'E', '1', 'B'],
# ⁠['B', '1', 'M', '1', 'B'],
# ⁠['B', '1', '1', '1', 'B'],
# ⁠['B', 'B', 'B', 'B', 'B']]
#
# Explanation:
#
#
#
#
# Example 2:
#
# Input:
#
# [['B', '1', 'E', '1', 'B'],
# ⁠['B', '1', 'M', '1', 'B'],
# ⁠['B', '1', '1', '1', 'B'],
# ⁠['B', 'B', 'B', 'B', 'B']]
#
# Click : [1,2]
#
# Output:
#
# [['B', '1', 'E', '1', 'B'],
# ⁠['B', '1', 'X', '1', 'B'],
# ⁠['B', '1', '1', '1', 'B'],
# ⁠['B', 'B', 'B', 'B', 'B']]
#
# Explanation:
#
#
#
#
#
#
# Note:
#
# The range of the input matrix's height and width is [1,50].
# The click position will only be an unrevealed square ('M' or 'E'), which also
# means the input board contains at least one clickable square.
# The input board won't be a stage when game is over (some mines have been
# revealed).
# For simplicity, not mentioned rules should be ignored in this problem. For
# example, you don't need to reveal all the unrevealed mines when the game is
# over, consider any cases that you will win the game or flag any squares.
#


class Solution:
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        self.dx = [1,0,0,-1,1,1,-1,-1]
        self.dy = [0,1,-1,0,1,-1,1,-1]
        nxt = board[:]
        x, y = click[0], click[1]
        if board[x][y] == 'M':
            nxt[x][y] = 'X'
            return nxt
        elif board[x][y] == 'E':
            self.res = self.getRes(board)
            if self.res[x][y] == 0:
                nxt[x][y] = 'B'
                self.click(board, x, y, nxt)
            else:
                nxt[x][y] = str(self.res[x][y])
            return nxt

    def getRes(self, board):
        res = [[0]*len(board[0]) for x in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                cnt = 0
                for d in range(8):
                    nx, ny = i+self.dx[d], j+self.dy[d]
                    if nx >= 0 and nx < len(board) and\
                            ny >= 0 and ny < len(board[0]):
                        if board[nx][ny] == 'M':
                            cnt += 1
                res[i][j] = cnt
        return res

    def click(self, board, x, y, nxt):
        for d in range(8):
            nx, ny = x+self.dx[d], y+self.dy[d]
            if nx >= 0 and nx < len(board) and\
                    ny >= 0 and ny < len(board[0]):
                if nxt[nx][ny] == 'E':
                    if self.res[nx][ny] == 0:
                        nxt[nx][ny] = 'B'
                        self.click(board, nx, ny, nxt)
                    else:
                        nxt[nx][ny] = str(self.res[nx][ny])
