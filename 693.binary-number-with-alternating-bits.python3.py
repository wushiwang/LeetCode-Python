#
# [693] Binary Number with Alternating Bits
#
# https://leetcode.com/problems/binary-number-with-alternating-bits/description/
#
# algorithms
# Easy (56.30%)
# Total Accepted:    26.6K
# Total Submissions: 47.3K
# Testcase Example:  '5'
#
# Given a positive integer, check whether it has alternating bits: namely, if
# two adjacent bits will always have different values.
#
# Example 1:
#
# Input: 5
# Output: True
# Explanation:
# The binary representation of 5 is: 101
#
#
#
# Example 2:
#
# Input: 7
# Output: False
# Explanation:
# The binary representation of 7 is: 111.
#
#
#
# Example 3:
#
# Input: 11
# Output: False
# Explanation:
# The binary representation of 11 is: 1011.
#
#
#
# Example 4:
#
# Input: 10
# Output: True
# Explanation:
# The binary representation of 10 is: 1010.
#


class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        i = 0
        one = True if n&1 == 1 else False
        n >>= 1
        while n != 0:
            if n&1 == 1:
                if one:
                    return False
                else:
                    one = True
            else:
                if not one:
                    return False
                else:
                    one = False
            n >>= 1
            i += 1
        return True
