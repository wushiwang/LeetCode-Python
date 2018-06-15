#
# [173] Binary Search Tree Iterator
#
# https://leetcode.com/problems/binary-search-tree-iterator/description/
#
# algorithms
# Medium (43.95%)
# Total Accepted:    135.5K
# Total Submissions: 308.2K
# Testcase Example:  '[]'
#
# Implement an iterator over a binary search tree (BST). Your iterator will be
# initialized with the root node of a BST.
#
# Calling next() will return the next smallest number in the BST.
#
# Note: next() and hasNext() should run in average O(1) time and uses O(h)
# memory, where h is the height of the tree.
#
# Credits:Special thanks to @ts for adding this problem and creating all test
# cases.
#
# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        if root is None:
            self.stack = []
        else:
            if root.left is None and root.right is None:
                self.stack = [root.val]
            else:
                self.stack = [root]

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.stack) != 0

    def next(self):
        """
        :rtype: int
        """
        cur = self.stack.pop()
        while type(cur) is TreeNode:
            if cur.right is not None:
                self.stack.append(cur.right)
            self.stack.append(cur.val)
            if cur.left is not None:
                self.stack.append(cur.left)
            cur = self.stack.pop()
        return cur

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
