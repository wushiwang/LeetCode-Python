#
# [716] Max Stack
#
# https://leetcode.com/problems/max-stack/description/
#
# algorithms
# Hard (36.80%)
# Total Accepted:    6.6K
# Total Submissions: 18K
# Testcase Example:  '["MaxStack","push","push","push","top","popMax","top","peekMax","pop","top"]\n[[],[5],[1],[5],[],[],[],[],[],[]]'
#
# Design a max stack that supports push, pop, top, peekMax and popMax.
#
#
#
# push(x) -- Push element x onto stack.
# pop() -- Remove the element on top of the stack and return it.
# top() -- Get the element on the top.
# peekMax() -- Retrieve the maximum element in the stack.
# popMax() -- Retrieve the maximum element in the stack, and remove it. If you
# find more than one maximum elements, only remove the top-most one.
#
#
#
# Example 1:
#
# MaxStack stack = new MaxStack();
# stack.push(5);
# stack.push(1);
# stack.push(5);
# stack.top(); -> 5
# stack.popMax(); -> 5
# stack.top(); -> 1
# stack.peekMax(); -> 5
# stack.pop(); -> 1
# stack.top(); -> 5
#
#
#
# Note:
#
# -1e7
# Number of operations won't exceed 10000.
# The last four operations won't be called when stack is empty.
#
# Solution based on two stacks, not the best time complexity
# Can be done better.


class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.lar = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if len(self.lar) == 0:
            self.lar.append(x)
        else:
            self.lar.append(max(self.lar[-1], x))

    def pop(self):
        """
        :rtype: int
        """
        res = self.stack.pop()
        self.lar.pop()
        return res

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        return self.lar[-1]

    def popMax(self):
        """
        :rtype: int
        """
        tmp = []
        while self.stack[-1] != self.lar[-1]:
            tmp.append(self.stack.pop())
            self.lar.pop()
        res = self.stack.pop()
        self.lar.pop()
        while len(tmp) != 0:
            self.push(tmp.pop())
        return res


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
