#
# [87] Scramble String
#
# https://leetcode.com/problems/scramble-string/description/
#
# algorithms
# Hard (29.85%)
# Total Accepted:    74.9K
# Total Submissions: 250.8K
# Testcase Example:  '"great"\n"rgeat"'
#
# Given a string s1, we may represent it as a binary tree by partitioning it to
# two non-empty substrings recursively.
#
# Below is one possible representation of s1 = "great":
#
#
# ⁠   great
# ⁠  /    \
# ⁠ gr    eat
# ⁠/ \    /  \
# g   r  e   at
# ⁠          / \
# ⁠         a   t
#
#
# To scramble the string, we may choose any non-leaf node and swap its two
# children.
#
# For example, if we choose the node "gr" and swap its two children, it
# produces a scrambled string "rgeat".
#
#
# ⁠   rgeat
# ⁠  /    \
# ⁠ rg    eat
# ⁠/ \    /  \
# r   g  e   at
# ⁠          / \
# ⁠         a   t
#
#
# We say that "rgeat" is a scrambled string of "great".
#
# Similarly, if we continue to swap the children of nodes "eat" and "at", it
# produces a scrambled string "rgtae".
#
#
# ⁠   rgtae
# ⁠  /    \
# ⁠ rg    tae
# ⁠/ \    /  \
# r   g  ta  e
# ⁠      / \
# ⁠     t   a
#
#
# We say that "rgtae" is a scrambled string of "great".
#
# Given two strings s1 and s2 of the same length, determine if s2 is a
# scrambled string of s1.
#
# Example 1:
#
#
# Input: s1 = "great", s2 = "rgeat"
# Output: true
#
#
# Example 2:
#
#
# Input: s1 = "abcde", s2 = "caebd"
# Output: false
#
import collections


class Solution:
    def __init__(self):
        self.dict = {}

    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            return False
        if s1+s2 in self.dict:
            return self.dict[s1+s2]
        if s1 == s2:
            self.dict[s1+s2] = True
            return True
        cnt = collections.Counter()
        for i in range(len(s1)):
            cnt[s1[i]] += 1
            cnt[s2[i]] -= 1
        for i in cnt:
            if cnt[i] != 0:
                self.dict[s1+s2] = False
                return False
        for i in range(1, len(s1)):
            if (self.isScramble(s1[:i], s2[:i]) and\
                    self.isScramble(s1[i:], s2[i:])) or\
                    (self.isScramble(s1[i:], s2[:-i]) and\
                     self.isScramble(s1[:i], s2[-i:])):
                self.dict[s1+s2] = True
                return True
        self.dict[s1+s2] = False
        return False
