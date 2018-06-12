#
# [140] Word Break II
#
# https://leetcode.com/problems/word-break-ii/description/
#
# algorithms
# Hard (24.75%)
# Total Accepted:    117K
# Total Submissions: 472.1K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, add spaces in s to construct a sentence where each word is a
# valid dictionary word. Return all such possible sentences.
#
# Note:
#
#
# The same word in the dictionary may be reused multiple times in the
# segmentation.
# You may assume the dictionary does not contain duplicate words.
#
#
# Example 1:
#
#
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
# "cats and dog",
# "cat sand dog"
# ]
#
#
# Example 2:
#
#
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
# "pine apple pen apple",
# "pineapple pen apple",
# "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
#
#
# Example 3:
#
#
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []
#


class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if len(wordDict) == 0:
            return []
        dic, dp = set(wordDict), [[] for x in range(len(s)+1)]
        dp[0].append(-1)
        for i in range(1, len(s)+1):
            for j in range(0, i):
                if len(dp[j]) != 0 and s[j:i] in dic:
                    dp[i].append(j)
        res = []
        self.DFS(len(s), dp, res, [], s)
        return [' '.join(r) for r in res]

    def DFS(self, pos, dp, res, cur, s):
        for nex in dp[pos]:
            if nex == 0:
                res.append([s[nex:pos]]+cur)
            else:
                self.DFS(nex, dp, res, [s[nex:pos]]+cur, s)
