#
# [411] Minimum Unique Word Abbreviation
#
# https://leetcode.com/problems/minimum-unique-word-abbreviation/description/
#
# algorithms
# Hard (33.81%)
# Total Accepted:    8K
# Total Submissions: 23.7K
# Testcase Example:  '"apple"\n["blade"]'
#
# A string such as "word" contains the following abbreviations:
#
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1",
# "w1r1", "1o2", "2r1", "3d", "w3", "4"]
#
#
# Given a target string and a set of strings in a dictionary, find an
# abbreviation of this target string with the smallest possible length such
# that it does not conflict with abbreviations of the strings in the
# dictionary.
#
# Each number or letter in the abbreviation is considered length = 1. For
# example, the abbreviation "a32bc" has length = 4.
#
# Note:
#
# In the case of multiple answers as shown in the second example below, you may
# return any one of them.
# Assume length of target string = m, and dictionary size = n. You may assume
# that m ≤ 21, n ≤ 1000, and log2(n) + m ≤ 20.
#
#
#
# Examples:
#
# "apple", ["blade"] -> "a4" (because "5" or "4e" conflicts with "blade")
#
# "apple", ["plain", "amber", "blade"] -> "1p3" (other valid answers include
# "ap3", "a3e", "2p2", "3le", "3l1").
#


class Solution:
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        # Get all abbreviation of target first
        self.dictionary = list(filter(lambda x:len(x) == len(target), dictionary))
        if len(self.dictionary) == 0:
            return str(len(target))
        self.res = target + '1'
        self.DFS(target, 0, "", 0)
        return self.res

    def DFS(self, word, num, cur, l):
            if word == '':
                if num != 0:
                    cur += str(num)
                    l += 1
                if len(cur) < len(self.res):
                    for w in self.dictionary:
                        if self.check(w, cur):
                            return
                    self.res = cur
                return
            self.DFS(word[1:], num+1, cur, l)
            nxt = cur+str(num)+word[0] if num != 0 else cur+word[0]
            le = l+2 if num != 0 else l+1
            self.DFS(word[1:], 0, nxt, le)

    def check(self, word, abbr):
        i, cur, lst = 0, 0, []
        while i < len(abbr):
            if ord(abbr[i]) >= ord('0') and ord(abbr[i]) <= ord('9'):
                cur *= 10
                cur += int(abbr[i])
            else:
                if cur != 0:
                    lst.append(cur)
                    cur = 0
                lst.append(abbr[i])
            i += 1
        if cur != 0:
            lst.append(cur)
        i, j = 0, 0
        while i < len(word) and j < len(lst):
            if type(lst[j]) is int:
                i, j = i+lst[j], j+1
            else:
                if word[i] != lst[j]:
                    return False
                i, j = i+1, j+1
        if i == len(word) and j == len(lst):
            return True
        return False
