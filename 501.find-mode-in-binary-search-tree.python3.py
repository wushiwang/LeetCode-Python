#
# [501] Find Mode in Binary Search Tree
#
# https://leetcode.com/problems/find-mode-in-binary-search-tree/description/
#
# algorithms
# Easy (37.79%)
# Total Accepted:    38.3K
# Total Submissions: 101.3K
# Testcase Example:  '[1,null,2,2]'
#
# Given a binary search tree (BST) with duplicates, find all the mode(s) (the
# most frequently occurred element) in the given BST.
#
# Assume a BST is defined as follows:
#
#
# The left subtree of a node contains only nodes with keys less than or equal
# to the node's key.
# The right subtree of a node contains only nodes with keys greater than or
# equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
#
#
# For example:
# Given BST [1,null,2,2],
#
#
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  2
#
#
#
#
# return [2].
#
# Note: If a tree has more than one mode, you can return them in any order.
#
# Follow up: Could you do that without using any extra space? (Assume that the
# implicit stack space incurred due to recursion does not count).
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.pre = None
        self.maxx = 0
        self.cur = 0
        self.res = []
        self.inner(root)
        return self.res

    def inner(self, root):
        if root is None:
            return
        self.inner(root.left)
        if self.pre is not None:
            if root.val == self.pre.val:
                self.cur += 1
                if self.cur > self.maxx:
                    self.maxx = self.cur
                    self.res = [root.val]
                elif self.cur == self.maxx:
                    self.res.append(root.val)
            else:
                self.cur = 1
                if self.cur == self.maxx:
                    self.res.append(root.val)
        else:
            self.cur = 1
            self.maxx = 1
            self.res = [root.val]
        self.pre = root
        self.inner(root.right)
