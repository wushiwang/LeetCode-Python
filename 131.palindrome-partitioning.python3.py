#
# [131] Palindrome Partitioning
#
# https://leetcode.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (36.15%)
# Total Accepted:    123.3K
# Total Submissions: 340.7K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
#
# Return all possible palindrome partitioning of s.
#
# Example:
#
#
# Input: "aab"
# Output:
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
#


class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        self.DFS(s, res, [], set())
        return res

    def DFS(self, s, res, cur, dic):
        if s in dic:
            res.append(cur+ [s])
        elif s == s[::-1]:
            dic.add(s)
            res.append(cur + [s])

        for i in range(1, len(s)):
            L, R = s[:i], s[i:]
            if L in dic:
                self.DFS(R, res, cur + [L], dic)
            elif L == L[::-1]:
                dic.add(L)
                self.DFS(R, res, cur + [L], dic)
