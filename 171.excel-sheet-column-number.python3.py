#
# [171] Excel Sheet Column Number
#
# https://leetcode.com/problems/excel-sheet-column-number/description/
#
# algorithms
# Easy (48.96%)
# Total Accepted:    172.4K
# Total Submissions: 352K
# Testcase Example:  '"A"'
#
# Given a column title as appear in an Excel sheet, return its corresponding
# column number.
#
# For example:
#
#
# ⁠   A -> 1
# ⁠   B -> 2
# ⁠   C -> 3
# ⁠   ...
# ⁠   Z -> 26
# ⁠   AA -> 27
# ⁠   AB -> 28
# ⁠   ...
#
#
# Example 1:
#
#
# Input: "A"
# Output: 1
#
#
# Example 2:
#
#
# Input: "AB"
# Output: 28
#
#
# Example 3:
#
#
# Input: "ZY"
# Output: 701
#


class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        base = ord('A')
        res, cur = 0, 26
        for i in range(len(s)-1):
            res += cur
            cur *= 26
        tmp = 26**(len(s)-1)
        for i in range(len(s)-1):
            res += (ord(s[i])-base)*tmp
            tmp //= 26
        res += ord(s[-1])-base+1
        return res
