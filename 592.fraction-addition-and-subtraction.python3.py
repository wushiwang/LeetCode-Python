#
# [592] Fraction Addition and Subtraction
#
# https://leetcode.com/problems/fraction-addition-and-subtraction/description/
#
# algorithms
# Medium (46.04%)
# Total Accepted:    9.3K
# Total Submissions: 20.2K
# Testcase Example:  '"-1/2+1/2"'
#
# Given a string representing an expression of fraction addition and
# subtraction, you need to return the calculation result in string format. The
# final result should be irreducible fraction. If your final result is an
# integer, say 2, you need to change it to the format of fraction that has
# denominator 1. So in this case, 2 should be converted to 2/1.
#
# Example 1:
#
# Input:"-1/2+1/2"
# Output: "0/1"
#
#
#
# Example 2:
#
# Input:"-1/2+1/2+1/3"
# Output: "1/3"
#
#
#
# Example 3:
#
# Input:"1/3-1/2"
# Output: "-1/6"
#
#
#
# Example 4:
#
# Input:"5/3+1/3"
# Output: "2/1"
#
#
#
# Note:
#
# The input string only contains '0' to '9', '/', '+' and '-'. So does the
# output.
# Each fraction (input and output) has format ±numerator/denominator. If the
# first input fraction or the output is positive, then '+' will be omitted.
# The input only contains valid irreducible fractions, where the numerator and
# denominator of each fraction will always be in the range [1,10]. If the
# denominator is 1, it means this fraction is actually an integer in a fraction
# format defined above.
# The number of given fractions will be in the range [1,10].
# The numerator and denominator of the final result are guaranteed to be valid
# and in the range of 32-bit int.
#


class Solution:
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        if len(expression) == 0:
            return ""
        if expression[0] != '-':
            expression = '+' + expression
        i, lst = 0, []
        while i < len(expression):
            cur = self.nextTocken(expression, i)
            i += len(cur)
            cur = cur.split('/')
            lst.append((int(cur[0]), int(cur[1])))
        D = 1
        for i in range(len(lst)):
            D *= lst[i][1]
        U = 0
        for i in range(len(lst)):
            U += lst[i][0]*(D//lst[i][1])
        if U == 0:
            return '0/1'
        elif U < 0:
            gcd = self.gcd(-U, D)
        else:
            gcd = self.gcd(U, D)
        return str(U//gcd) + '/' + str(D//gcd)

    def nextTocken(self, expression, pos):
        start = pos
        pos += 1
        while pos < len(expression):
            if expression[pos] == '+' or expression[pos] == '-':
                break
            pos += 1
        return expression[start: pos]

    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)