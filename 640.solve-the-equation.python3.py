#
# [640] Solve the Equation
#
# https://leetcode.com/problems/solve-the-equation/description/
#
# algorithms
# Medium (38.73%)
# Total Accepted:    10.8K
# Total Submissions: 27.8K
# Testcase Example:  '"x+5-3+x=6+x-2"'
#
#
# Solve a given equation and return the value of x in the form of string
# "x=#value". The equation contains only '+', '-' operation, the variable x and
# its coefficient.
#
#
#
# If there is no solution for the equation, return "No solution".
#
#
# If there are infinite solutions for the equation, return "Infinite
# solutions".
#
#
# If there is exactly one solution for the equation, we ensure that the value
# of x is an integer.
#
#
# Example 1:
#
# Input: "x+5-3+x=6+x-2"
# Output: "x=2"
#
#
#
# Example 2:
#
# Input: "x=x"
# Output: "Infinite solutions"
#
#
#
# Example 3:
#
# Input: "2x=x"
# Output: "x=0"
#
#
#
# Example 4:
#
# Input: "2x+3x-6x=x+2"
# Output: "x=-1"
#
#
#
# Example 5:
#
# Input: "x=x+2"
# Output: "No solution"
#


class Solution:
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        L, R = equation.split('=')
        lv, lx = self.scanner(L)
        rv, rx = self.scanner(R)
        v = rv - lv
        x = lx - rx
        if x == 0 and v != 0:
            return 'No solution'
        elif x == 0 and v == 0:
            return 'Infinite solutions'
        else:
            return 'x=' + str(v//x)

    def scanner(self, s):
        v, x = 0, 0
        if s[0] != '-':
            s = '+' + s
        i = 0
        while i < len(s):
            L = i+1
            while L < len(s) and s[L].isdigit():
                L += 1
            cur = s[i:L]
            if L < len(s) and s[L] == 'x':
                if len(cur) == 1:
                    x += int(cur+'1')
                else:
                    x += int(cur)
                i = L+1
            else:
                v += int(cur)
                i = L
        return v, x
