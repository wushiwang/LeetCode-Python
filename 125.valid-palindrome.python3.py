#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (27.46%)
# Total Accepted:    234.4K
# Total Submissions: 853.1K
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
#
# Example 1:
#
#
# Input: "A man, a plan, a canal: Panama"
# Output: true
#
#
# Example 2:
#
#
# Input: "race a car"
# Output: false
#


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.upper()
        s = ' '.join(list(filter(lambda x: (x >= 'A' and x <= 'Z') or (x >= '0' and x <='9'), list(s))))
        return s == s[::-1]
