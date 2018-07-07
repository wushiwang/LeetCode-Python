#
# [405] Convert a Number to Hexadecimal
#
# https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/
#
# algorithms
# Easy (41.16%)
# Total Accepted:    36.3K
# Total Submissions: 88.1K
# Testcase Example:  '26'
#
#
# Given an integer, write an algorithm to convert it to hexadecimal. For
# negative integer, two’s complement method is used.
#
#
# Note:
#
# All letters in hexadecimal (a-f) must be in lowercase.
# The hexadecimal string must not contain extra leading 0s. If the number is
# zero, it is represented by a single zero character '0'; otherwise, the first
# character in the hexadecimal string will not be the zero character.
# The given number is guaranteed to fit within the range of a 32-bit signed
# integer.
# You must not use any method provided by the library which converts/formats
# the number to hex directly.
#
#
#
# Example 1:
#
# Input:
# 26
#
# Output:
# "1a"
#
#
#
# Example 2:
#
# Input:
# -1
#
# Output:
# "ffffffff"
#


class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num < 0:
            num *= -1
            num = ((~num) + 1) & 0xffffffff
        lst = ['0', '1', '2', '3', '4', '5', '6', '7',
               '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        res = []
        for i in range(8):
            cur = 0
            for j in range(4):
                if ((num >> (i*4+j)) & 1) == 1:
                    cur += (1 << j)
            res.append(lst[cur])
        res = ''.join(res[::-1]).lstrip('0')
        return res if len(res) != 0 else '0'
