#
# [38] Count and Say
#
# https://leetcode.com/problems/count-and-say/description/
#
# algorithms
# Easy (37.02%)
# Total Accepted:    196.1K
# Total Submissions: 529.4K
# Testcase Example:  '1'
#
# The count-and-say sequence is the sequence of integers with the first five
# terms as following:
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
#
#
#
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
#
#
#
# Given an integer n, generate the nth term of the count-and-say sequence.
#
#
#
# Note: Each term of the sequence of integers will be represented as a
# string.
#
#
# Example 1:
#
# Input: 1
# Output: "1"
#
#
#
# Example 2:
#
# Input: 4
# Output: "1211"
#


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        for i in range(n-1):
            tmp, i = "", 0
            while i < len(s):
                j = i
                while j != len(s) - 1 and s[j] == s[j+1]:
                    j += 1
                tmp += str(j-i+1) + s[i]
                i = j + 1
            s = tmp
        return s
