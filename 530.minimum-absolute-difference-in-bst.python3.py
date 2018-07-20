#
# [530] Minimum Absolute Difference in BST
#
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
#
# algorithms
# Easy (47.99%)
# Total Accepted:    40.8K
# Total Submissions: 85K
# Testcase Example:  '[1,null,3,2]'
#
# Given a binary search tree with non-negative values, find the minimum
# absolute difference between values of any two nodes.
#
#
# Example:
#
# Input:
#
# ⁠  1
# ⁠   \
# ⁠    3
# ⁠   /
# ⁠  2
#
# Output:
# 1
#
# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1
# (or between 2 and 3).
#
#
#
#
# Note:
# There are at least two nodes in this BST.
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import math


class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.pre = None
        self.res = math.inf
        self.innerOrder(root)
        return self.res

    def innerOrder(self, root):
        if root is None:
            return
        self.innerOrder(root.left)
        if self.pre is not None:
            self.res = min(self.res, int(abs(root.val - self.pre)))
        self.pre = root.val
        self.innerOrder(root.right)
