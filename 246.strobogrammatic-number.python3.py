#
# [246] Strobogrammatic Number
#
# https://leetcode.com/problems/strobogrammatic-number/description/
#
# algorithms
# Easy (40.37%)
# Total Accepted:    36.9K
# Total Submissions: 91.4K
# Testcase Example:  '"69"'
#
# A strobogrammatic number is a number that looks the same when rotated 180
# degrees (looked at upside down).
#
# Write a function to determine if a number is strobogrammatic. The number is
# represented as a string.
#
# Example 1:
#
#
# Input:  "69"
# Output: true
#
#
# Example 2:
#
#
# Input:  "88"
# Output: true
#
# Example 3:
#
#
# Input:  "962"
# Output: false
#


class Solution:
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        imps = ['2', '3', '4', '5', '7']
        dic = {'1': '1',
               '6': '9',
               '8': '8',
               '9': '6',
               '0': '0'}
        for c in imps:
            if c in num:
                return False
        rev = ''.join([dic[x] for x in num[::-1]])
        return rev == num
