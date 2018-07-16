#
# [481] Magical String
#
# https://leetcode.com/problems/magical-string/description/
#
# algorithms
# Medium (45.77%)
# Total Accepted:    14.8K
# Total Submissions: 32.4K
# Testcase Example:  '1'
#
#
# A magical string S consists of only '1' and '2' and obeys the following
# rules:
#
#
# The string S is magical because concatenating the number of contiguous
# occurrences of characters '1' and '2' generates the string S itself.
#
#
#
# The first few elements of string S is the following:
# S = "1221121221221121122……"
#
#
#
# If we group the consecutive '1's and '2's in S, it will be:
#
#
# 1   22  11  2  1  22  1  22  11  2  11  22 ......
#
#
# and the occurrences of '1's or '2's in each group are:
#
#
# 1   2       2    1   1    2     1    2     2    1    2    2 ......
#
#
#
# You can see that the occurrence sequence above is the S itself.
#
#
#
# Given an integer N as input, return the number of '1's in the first N number
# in the magical string S.
#
#
# Note:
# N will not exceed 100,000.
#
#
#
# Example 1:
#
# Input: 6
# Output: 3
# Explanation: The first 6 elements of magical string S is "12211" and it
# contains three 1's, so return 3.
#


class Solution:
    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n <= 3:
            return 1
        a = ['1', '2', '2']
        res, i = 1, 2
        while len(a) < n:
            if a[i] == '1':
                if a[-1] == '1':
                    a.append('2')
                else:
                    a.append('1')
                    res += 1
            else:
                if a[-1] == '1':
                    a.append('2')
                    if len(a) == n:
                        break
                    a.append('2')
                else:
                    a.append('1')
                    res += 1
                    if len(a) == n:
                        break
                    a.append('1')
                    res += 1
            i += 1
        return res
