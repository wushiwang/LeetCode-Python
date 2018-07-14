#
# [466] Count The Repetitions
#
# https://leetcode.com/problems/count-the-repetitions/description/
#
# algorithms
# Hard (27.25%)
# Total Accepted:    6.2K
# Total Submissions: 22.8K
# Testcase Example:  '"acb"\n4\n"ab"\n2'
#
# Define S = [s,n] as the string S which consists of n connected strings s. For
# example, ["abc", 3] ="abcabcabc".
# On the other hand, we define that string s1 can be obtained from string s2 if
# we can remove some characters from s2 such that it becomes s1. For example,
# “abc”  can be obtained from “abdbec” based on our definition, but it can not
# be obtained from “acbbe”.
# You are given two non-empty strings s1 and s2 (each at most 100 characters
# long) and two integers 0 ≤ n1 ≤ 106 and 1 ≤ n2 ≤ 106. Now consider the
# strings S1 and S2, where S1=[s1,n1] and S2=[s2,n2]. Find the maximum integer
# M such that [S2,M] can be obtained from S1.
#
# Example:
#
# Input:
# s1="acb", n1=4
# s2="ab", n2=2
#
# Return:
# 2
#


class Solution:
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        self.dic = dict()
        n, res, R = 0, 0, 0
        while n < n1:
            line, R = self.match(s1, s2, 0, R)
            res += line
            n += 1
            if R == 0:
                res = (n1//n)*res
                n = n1 - (n1%n)
        return res // n2

    def match(self, s1, s2, L, R):
        if R in self.dic:
            return self.dic[R]
        res, start = 0, R
        while L < len(s1):
            if s1[L] == s2[R]:
                L, R = L+1, R+1
            else:
                L += 1
            if R == len(s2):
                res += 1
                R = 0
        self.dic[start] = (res, R)
        return (res, R)
