#
# [306] Additive Number
#
# https://leetcode.com/problems/additive-number/description/
#
# algorithms
# Medium (27.79%)
# Total Accepted:    32.1K
# Total Submissions: 115.6K
# Testcase Example:  '"112358"'
#
# Additive number is a string whose digits can form additive sequence.
#
# A valid additive sequence should contain at least three numbers. Except for
# the first two numbers, each subsequent number in the sequence must be the sum
# of the preceding two.
#
# Given a string containing only digits '0'-'9', write a function to determine
# if it's an additive number.
#
# Note: Numbers in the additive sequence cannot have leading zeros, so sequence
# 1, 2, 03 or 1, 02, 3 is invalid.
#
# Example 1:
#
#
# Input: "112358"
# Output: true
# Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5,
# 8.
# 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
#
#
# Example 2:
#
#
# Input: "199100199"
# Output: true
# Explanation: The additive sequence is: 1, 99, 100, 199. 
# 1 + 99 = 100, 99 + 100 = 199
#
# Follow up:
# How would you handle overflow for very large input integers?
#


class Solution:
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        # Enumerate first two numbers, then recursively check rest numbers
        for j in range(2, len(num)):
            cur = num[:j]
            for i in range(1, len(cur)):
                if (i == 1 or cur[0] != '0') and (i == len(cur)-1 or cur[i] != '0'):
                    a, b = int(cur[:i]), int(cur[i:])
                    if self.check(a, b, num[j:]):
                        return True
        return False

    def check(self, a, b, s):
        if s == '':
            return True
        if len(s) < len(str(b)):
            return False
        for i in range(1, len(s)+1):
            if (i == 1 or s[0] != '0') and int(s[:i]) == a+b:
                if self.check(b, int(s[:i]), s[i:]):
                    return True
        return False
