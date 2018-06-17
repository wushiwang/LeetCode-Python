#
# [212] Word Search II
#
# https://leetcode.com/problems/word-search-ii/description/
#
# algorithms
# Hard (25.23%)
# Total Accepted:    69K
# Total Submissions: 273.2K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],
# ["i","f","l","v"]]\n["oath","pea","eat","rain"]'
#
# Given a 2D board and a list of words from the dictionary, find all words in
# the board.
#
# Each word must be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring. The
# same letter cell may not be used more than once in a word.
#
# Example:
#
#
# Input:
# words = ["oath","pea","eat","rain"] and board =
# [
# ⁠ ['o','a','a','n'],
# ⁠ ['e','t','a','e'],
# ⁠ ['i','h','k','r'],
# ⁠ ['i','f','l','v']
# ]
#
# Output: ["eat","oath"]
#
#
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
#
import collections


class Solution:

    class Node:
        def __init__(self):
            self.isWord = False
            self.chd = dict()
            self.word = None

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if len(board) == 0:
            return []
        # DFS + Trie
        # Build a trie tree
        head = self.Node()
        for w in words:
            cur = head
            for c in w:
                if c not in cur.chd:
                    cur.chd[c] = self.Node()
                cur = cur.chd[c]
            cur.isWord = True
            cur.word = w
        # DFS
        self.dx = [1,0,0,-1]
        self.dy = [0,1,-1,0]
        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in head.chd:
                    visited = set()
                    visited.add((i, j))
                    self.DFS(i, j, board, head.chd[board[i][j]], visited, res)
        return res

    def DFS(self, x, y, board, node, visited, res):
        if node.isWord:
            res.append(node.word)
            node.isWord = False
        for i in range(4):
            nx, ny = x+self.dx[i], y+self.dy[i]
            if nx >= 0 and nx < len(board) and ny >= 0 and ny < len(board[0]):
                if (nx, ny) not in visited and board[nx][ny] in node.chd:
                    visited.add((nx, ny))
                    self.DFS(nx, ny, board, node.chd[board[nx][ny]],
                             visited, res)
                    visited.remove((nx, ny))
