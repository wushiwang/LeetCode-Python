#
# [241] Different Ways to Add Parentheses
#
# https://leetcode.com/problems/different-ways-to-add-parentheses/description/
#
# algorithms
# Medium (46.54%)
# Total Accepted:    57.3K
# Total Submissions: 123.1K
# Testcase Example:  '"2-1-1"'
#
# Given a string of numbers and operators, return all possible results from
# computing all the different possible ways to group numbers and operators. The
# valid operators are +, - and *.
#
# Example 1:
#
#
# Input: "2-1-1"
# Output: [0, 2]
# Explanation:
# ((2-1)-1) = 0
# (2-(1-1)) = 2
#
# Example 2:
#
#
# Input: "2*3-4*5"
# Output: [-34, -14, -10, -10, 10]
# Explanation:
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
#
import operator


class Solution:
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        self.opd = {'+': operator.add,
                    '-': operator.sub,
                    '*': operator.mul}
        # Tokenize input
        op, i = [], 0
        while i < len(input):
            c = input[i]
            if c == '+' or c == '-' or c == '*':
                op.append(c)
            else:
                j = i
                while j < len(input) and input[j].isdigit():
                    j += 1
                op.append(int(input[i:j]))
                i = j-1
            i += 1
        # Recursively solve the problem
        return self.helper(op)

    def helper(self, op):
        if len(op) == 1:
            return op
        res = []
        for i in range(len(op)):
            if type(op[i]) is str:
                res += [self.opd[op[i]](x, y) for x in self.helper(op[:i]) for y in self.helper(op[i+1:])]
        return res
