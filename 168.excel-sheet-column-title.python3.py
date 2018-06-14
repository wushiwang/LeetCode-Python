#
# [168] Excel Sheet Column Title
#
# https://leetcode.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (27.54%)
# Total Accepted:    139.3K
# Total Submissions: 505.9K
# Testcase Example:  '1'
#
# Given a positive integer, return its corresponding column title as appear in
# an Excel sheet.
#
# For example:
#
#
# ⁠   1 -> A
# ⁠   2 -> B
# ⁠   3 -> C
# ⁠   ...
# ⁠   26 -> Z
# ⁠   27 -> AA
# ⁠   28 -> AB
# ⁠   ...
#
#
# Example 1:
#
#
# Input: 1
# Output: "A"
#
#
# Example 2:
#
#
# Input: 28
# Output: "AB"
#
#
# Example 3:
#
#
# Input: 701
# Output: "ZY"
#


class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        base = ord('A')
        L, R, cur, k = 0, 26, 26, 0
        while True:
            if n > L and n <= R:
                break
            L += cur
            cur *= 26
            R += cur
            k += 1
        n -= L
        res = [chr(base+(n-1)%26)]
        while k > 0:
            if n == 0:
                res += ["A"]
            else:
                if n % 26 == 0:
                    n = (n-1) // 26
                else:
                    n //= 26
                res += [chr(base+n%26)]
            k -= 1
        return ''.join(res[::-1])
