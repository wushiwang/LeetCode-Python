#
# [282] Expression Add Operators
#
# https://leetcode.com/problems/expression-add-operators/description/
#
# algorithms
# Hard (30.72%)
# Total Accepted:    48.9K
# Total Submissions: 159.1K
# Testcase Example:  '"123"\n6'
#
# Given a string that contains only digits 0-9 and a target value, return all
# possibilities to add binary operators (not unary) +, -, or * between the
# digits so they evaluate to the target value.
#
# Example 1:
#
#
# Input: num = "123", target = 6
# Output: ["1+2+3", "1*2*3"]
#
#
# Example 2:
#
#
# Input: num = "232", target = 8
# Output: ["2*3+2", "2+3*2"]
#
# Example 3:
#
#
# Input: num = "105", target = 5
# Output: ["1*0+5","10-5"]
#
# Example 4:
#
#
# Input: num = "00", target = 0
# Output: ["0+0", "0-0", "0*0"]
#
#
# Example 5:
#
#
# Input: num = "3456237490", target = 9191
# Output: []
#


class Solution:
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        self.target = target
        self.res = []
        for i in range(1, len(num)+1):
            if i == 1 or num[0] != '0':
                self.DFS(num[i:], num[:i], int(num[:i]), 0, int(num[:i]))
        return self.res

    def DFS(self, num, s, v, pre, mul):
        if num == '' and v == self.target:
            self.res.append(s)

        for i in range(1, len(num)+1):
            cur = int(num[:i])
            if i == 1 or num[0] != '0':
                self.DFS(num[i:], s+'+'+num[:i], v+cur, v, cur)
                self.DFS(num[i:], s+'-'+num[:i], v-cur, v, -cur)
                self.DFS(num[i:], s+'*'+num[:i], pre+mul*cur, pre, mul*cur)
