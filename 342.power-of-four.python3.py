#
# [342] Power of Four
#
# https://leetcode.com/problems/power-of-four/description/
#
# algorithms
# Easy (39.34%)
# Total Accepted:    89K
# Total Submissions: 226.3K
# Testcase Example:  '16'
#
#
# Given an integer (signed 32 bits), write a function to check whether it is a
# power of 4.
#
# Example:
# Given num = 16, return true.
# Given num = 5, return false.
#
#
# Follow up: Could you solve it without loops/recursion?
#
# Credits:Special thanks to @yukuairoy  for adding this problem and creating
# all test cases.
#


class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        mask = 1431655765
        if num & (-num) == num and num & mask == num:
            return True
        return False
