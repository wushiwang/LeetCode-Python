#
# [438] Find All Anagrams in a String
#
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
#
# algorithms
# Easy (33.99%)
# Total Accepted:    69.3K
# Total Submissions: 203.7K
# Testcase Example:  '"cbaebabacd"\n"abc"'
#
# Given a string s and a non-empty string p, find all the start indices of p's
# anagrams in s.
#
# Strings consists of lowercase English letters only and the length of both
# strings s and p will not be larger than 20,100.
#
# The order of output does not matter.
#
# Example 1:
#
# Input:
# s: "cbaebabacd" p: "abc"
#
# Output:
# [0, 6]
#
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#
#
#
# Example 2:
#
# Input:
# s: "abab" p: "ab"
#
# Output:
# [0, 1, 2]
#
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
#
import collections


class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        cnt = collections.Counter(p)
        cur = collections.Counter(s[:len(p)])
        res = []
        if cur == cnt:
            res.append(0)
        for i in range(len(p), len(s)):
            cur[s[i-len(p)]] -= 1
            if cur[s[i-len(p)]] == 0:
                cur.pop(s[i-len(p)])
            cur[s[i]] += 1
            if cur == cnt:
                res.append(i-len(p)+1)
        return res
