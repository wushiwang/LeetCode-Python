#
# [269] Alien Dictionary
#
# https://leetcode.com/problems/alien-dictionary/description/
#
# algorithms
# Hard (26.78%)
# Total Accepted:    43K
# Total Submissions: 160.5K
# Testcase Example:  '["wrt","wrf","er","ett","rftt"]'
#
# There is a new alien language which uses the latin alphabet. However, the
# order among letters are unknown to you. You receive a list of non-empty words
# from the dictionary, where words are sorted lexicographically by the rules of
# this new language. Derive the order of letters in this language.
#
# Example 1:
#
#
# Input:
# [
# ⁠ "wrt",
# ⁠ "wrf",
# ⁠ "er",
# ⁠ "ett",
# ⁠ "rftt"
# ]
#
# Output: "wertf"
#
#
# Example 2:
#
#
# Input:
# [
# ⁠ "z",
# ⁠ "x"
# ]
#
# Output: "zx"
#
#
# Example 3:
#
#
# Input:
# [
# ⁠ "z",
# ⁠ "x",
# ⁠ "z"
# ]
#
# Output: "" 
#
# Explanation: The order is invalid, so return "".
#
#
# Note:
#
#
# You may assume all letters are in lowercase.
# You may assume that if a is a prefix of b, then a must appear before b in the
# given dictionary.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is
# fine.
#


class Solution:
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        def _getPrefix(a, b):
            i = 0
            while i < min(len(a), len(b)) and a[i] == b[i]:
                i += 1
            return i
        if len(words) == 0:
            return ""
        graph = dict()
        ind = [0 for x in range(26)]
        for i in range(1, len(words)):
            prefix = _getPrefix(words[i-1], words[i])
            if prefix < len(words[i-1]) and prefix < len(words[i]):
                l, r = words[i-1][prefix], words[i][prefix]
                if l not in graph:
                    graph[l] = set()
                if r not in graph:
                    graph[r] = set()
                if r not in graph[l]:
                    graph[l].add(r)
                    ind[ord(r)-ord('a')] += 1
        wordset = set()
        for word in words:
            wordset |= set(word)
        # Top logical sort
        que, res = [], ""
        for i in range(26):
            if ind[i] == 0 and chr(i+ord('a')) in wordset:
                que.append(chr(i+ord('a')))
        print(que)
        while len(que) != 0:
            cur = que.pop()
            if cur in graph:
                res += cur
                for r in graph[cur]:
                    ind[ord(r)-ord('a')] -= 1
                    if ind[ord(r)-ord('a')] == 0:
                        que.append(r)
                graph[cur].clear()
            else:
                res += cur
        if len(res) != len(wordset):
            return ""
        return res
