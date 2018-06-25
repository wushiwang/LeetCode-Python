#
# [291] Word Pattern II
#
# https://leetcode.com/problems/word-pattern-ii/description/
#
# algorithms
# Hard (38.66%)
# Total Accepted:    23.4K
# Total Submissions: 60.6K
# Testcase Example:  '"abab"\n"redblueredblue"'
#
# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty substring in str.
#
# Example 1:
#
#
# Input: pattern = "abab", str = "redblueredblue"
# Output: true
#
# Example 2:
#
#
# Input: pattern = pattern = "aaaa", str = "asdasdasdasd"
# Output: true
#
# Example 3:
#
#
# Input: pattern = "aabb", str = "xyzabcxzyabc"
# Output: false
#
#
# Notes:
# You may assume both pattern and str contains only lowercase letters.
#


class Solution:
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        ab, ba = dict(), dict()
        return self.DFS(pattern, str, ab, ba)

    def DFS(self, pattern, str, ab, ba):
        if pattern == '' and str == '':
            return True
        if pattern == '' or str == '':
            return False
        for i in range(1, len(str)-len(pattern)+2):
            L, R = pattern[0], str[:i]
            flag = False
            if L not in ab and R not in ba:
                ab[L], ba[R] = R, L
                flag = True
            elif not (L in ab and R in ba and
                      ab[L] == R and ba[R] == L):
                continue
            res = self.DFS(pattern[1:], str[i:], ab, ba)
            if flag:
                ab.pop(L)
                ba.pop(R)
            if res:
                return True
        return False
