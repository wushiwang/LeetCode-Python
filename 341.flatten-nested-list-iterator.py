#
# [341] Flatten Nested List Iterator
#
# https://leetcode.com/problems/flatten-nested-list-iterator/description/
#
# algorithms
# Medium (43.68%)
# Total Accepted:    68.4K
# Total Submissions: 156.5K
# Testcase Example:  '[[1,1],2,[1,1]]'
#
# Given a nested list of integers, implement an iterator to flatten it.
#
# Each element is either an integer, or a list -- whose elements may also be
# integers or other lists.
#
# Example 1:
# Given the list [[1,1],2,[1,1]],
#
# By calling next repeatedly until hasNext returns false, the order of elements
# returned by next should be: [1,1,2,1,1].
#
#
#
# Example 2:
# Given the list [1,[4,[6]]],
#
# By calling next repeatedly until hasNext returns false, the order of elements
# returned by next should be: [1,4,6].
#
#
#
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = [[nestedList, 0]]

    def next(self):
        """
        :rtype: int
        """
        res = self.stack[-1][0][self.stack[-1][1]]
        self.stack[-1][1] += 1
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        while True:
            l, i = self.stack[-1]
            if i == len(l):
                self.stack.pop()
                if len(self.stack) == 0:
                    return False
                else:
                    self.stack[-1][1] += 1
            elif not l[i].isInteger():
                self.stack.append([l[i].getList(), 0])
            else:
                break
        return True

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
