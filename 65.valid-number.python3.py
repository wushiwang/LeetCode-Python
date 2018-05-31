#
# [65] Valid Number
#
# https://leetcode.com/problems/valid-number/description/
#
# algorithms
# Hard (12.95%)
# Total Accepted:    87.3K
# Total Submissions: 674.3K
# Testcase Example:  '"0"'
#
# Validate if a given string is numeric.
#
# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
#
# Note: It is intended for the problem statement to be ambiguous. You should
# gather all requirements up front before implementing one.
#
# Update (2015-02-10):
# The signature of the C++ function had been updated. If you still see your
# function signature accepts a const char * argument, please click the reload
# button to reset your code definition.
#
#
import re


class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pattern = re.compile(r"^[ ]*[+-]?((\d+(\.\d*)?)|(\.\d+))(e[+-]?\d+)?[ ]*$")
        return True if pattern.match(s) else False
