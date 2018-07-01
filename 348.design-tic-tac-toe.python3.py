#
# [348] Design Tic-Tac-Toe
#
# https://leetcode.com/problems/design-tic-tac-toe/description/
#
# algorithms
# Medium (46.32%)
# Total Accepted:    25.4K
# Total Submissions: 54.9K
# Testcase Example:  '["TicTacToe","move","move","move","move","move","move","move"]\n[[3],[0,0,1],[0,2,2],[2,2,1],[1,1,2],[2,0,1],[1,0,2],[2,1,1]]'
#
# Design a Tic-tac-toe game that is played between two players on a n x n
# grid.
#
#
# You may assume the following rules:
#
# A move is guaranteed to be valid and is placed on an empty block.
# Once a winning condition is reached, no more moves is allowed.
# A player who succeeds in placing n of their marks in a horizontal, vertical,
# or diagonal row wins the game.
#
#
#
# Example:
#
# Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.
#
# TicTacToe toe = new TicTacToe(3);
#
# toe.move(0, 0, 1); -> Returns 0 (no one wins)
# |X| | |
# | | | |    // Player 1 makes a move at (0, 0).
# | | | |
#
# toe.move(0, 2, 2); -> Returns 0 (no one wins)
# |X| |O|
# | | | |    // Player 2 makes a move at (0, 2).
# | | | |
#
# toe.move(2, 2, 1); -> Returns 0 (no one wins)
# |X| |O|
# | | | |    // Player 1 makes a move at (2, 2).
# | | |X|
#
# toe.move(1, 1, 2); -> Returns 0 (no one wins)
# |X| |O|
# | |O| |    // Player 2 makes a move at (1, 1).
# | | |X|
#
# toe.move(2, 0, 1); -> Returns 0 (no one wins)
# |X| |O|
# | |O| |    // Player 1 makes a move at (2, 0).
# |X| |X|
#
# toe.move(1, 0, 2); -> Returns 0 (no one wins)
# |X| |O|
# |O|O| |    // Player 2 makes a move at (1, 0).
# |X| |X|
#
# toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
# |X| |O|
# |O|O| |    // Player 1 makes a move at (2, 1).
# |X|X|X|
#
#
#
# Follow up:
# Could you do better than O(n2) per move() operation?
#
#
class TicTacToe:

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.board = [[0 for x in range(n)] for y in range(n)]
        self.n = n

    def _check_dia(self, x, y):
        if x == y and x == self.n-1-y:
            return self._check_dia1() or self._check_dia2()
        if x == y:
            return self._check_dia1()
        if x == self.n-1-y:
            return self._check_dia2()
        return False

    def _check_dia1(self):
        i, j = 1, 1
        while i < self.n and j < self.n:
            if self.board[i][j] != self.board[i-1][j-1]:
                return False
            i, j = i+1, j+1
        return True

    def _check_dia2(self):
        i, j = 1, self.n-2
        while i < self.n and j >= 0:
            if self.board[i][j] != self.board[i-1][j+1]:
                return False
            i, j = i+1, j-1
        return True

    def _check_hor(self, i):
        j = 1
        while j < self.n:
            if self.board[i][j] != self.board[i][j-1]:
                return False
            j += 1
        return True

    def _check_ver(self, j):
        i = 1
        while i < self.n:
            if self.board[i][j] != self.board[i-1][j]:
                return False
            i += 1
        return True

    def _check(self, i, j):
        return self._check_dia(i, j) or self._check_hor(i) or self._check_ver(j)

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        if self.n == 1:
            return player
        self.board[row][col] = player
        if self._check(row, col):
            return player
        else:
            return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
