#
# [186] Reverse Words in a String II
#
# https://leetcode.com/problems/reverse-words-in-a-string-ii/description/
#
# algorithms
# Medium (31.26%)
# Total Accepted:    44K
# Total Submissions: 140.4K
# Testcase Example:  '["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]'
#
# Given an input string , reverse the string word by word. 
#
# Example:
#
#
# Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
# Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]
#
# Note: 
#
#
# A word is defined as a sequence of non-space characters.
# The input string does not contain leading or trailing spaces.
# The words are always separated by a single space.
#
#
# Follow up: Could you do it in-place without allocating extra space?
#


class Solution:
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        # One line solution
        # str[:] = list(' '.join(''.join(str).split()[::-1]))

        # In-place solution (O(1) extra space)
        # Step 1: Reverse the str
        L, R = 0, len(str)-1
        while L < R:
            str[L], str[R] = str[R], str[L]
            L, R = L+1, R-1
        # Step 2: Reverse the words
        L, R = 0, 0
        while R < len(str):
            while R < len(str) and str[R] != ' ':
                R += 1
            a, b = L, R-1
            while a < b:
                str[a], str[b] = str[b], str[a]
                a, b = a+1, b-1
            L = R = R + 1
        if L != R:
            a, b = L, R-1
            while a < b:
                str[a], str[b] = str[b], str[a]
                a, b = a+1, b-1
        return

