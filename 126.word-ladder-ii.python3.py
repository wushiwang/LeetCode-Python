#
# [126] Word Ladder II
#
# https://leetcode.com/problems/word-ladder-ii/description/
#
# algorithms
# Hard (15.05%)
# Total Accepted:    84.8K
# Total Submissions: 563.2K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# Given two words (beginWord and endWord), and a dictionary's word list, find
# all shortest transformation sequence(s) from beginWord to endWord, such
# that:
#
#
# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
#
#
# Note:
#
#
# Return an empty list if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
#
#
# Example 1:
#
#
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output:
# [
# ⁠ ["hit","hot","dot","dog","cog"],
# ["hit","hot","lot","log","cog"]
# ]
#
#
# Example 2:
#
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: []
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible
# transformation.
#
import string


class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList, graph = set(wordList) | {beginWord}, dict()
        current_que, next_que, flag = {beginWord}, set(), False

        while len(current_que) != 0:
            for cur in current_que:
                if cur == endWord:
                    flag = True
                    break
                for i in range(len(beginWord)):
                    for j in string.ascii_lowercase:
                        next_word = cur[:i]+j+cur[i+1:]
                        if next_word not in current_que and next_word in wordList:
                            next_que.add(next_word)
                            if cur not in graph:
                                graph[cur] = {next_word}
                            else:
                                graph[cur].add(next_word)
            if flag:
                break
            for cur in current_que:
                wordList.remove(cur)
            current_que = next_que
            next_que = set()

        if not flag:
            return []
        else:
            self.res, self.cur = [], [beginWord]
            self.DFS(endWord, graph)
            return self.res

    def DFS(self, endWord, graph):
        if self.cur[-1] == endWord:
            self.res.append(list(self.cur))
            return
        if self.cur[-1] in graph:
            for next_word in graph[self.cur[-1]]:
                self.cur.append(next_word)
                self.DFS(endWord, graph)
                self.cur.pop()
