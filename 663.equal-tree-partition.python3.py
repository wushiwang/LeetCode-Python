#
# [663] Equal Tree Partition
#
# https://leetcode.com/problems/equal-tree-partition/description/
#
# algorithms
# Medium (36.42%)
# Total Accepted:    9.3K
# Total Submissions: 25.4K
# Testcase Example:  '[5,10,10,null,null,2,3]'
#
#
# Given a binary tree with n nodes, your task is to check if it's possible to
# partition the tree to two trees which have the equal sum of values after
# removing exactly one edge on the original tree.
#
#
# Example 1:
#
# Input:
# ⁠   5
# ⁠  / \
# ⁠ 10 10
# ⁠   /  \
# ⁠  2   3
#
# Output: True
# Explanation:
# ⁠   5
# ⁠  /
# ⁠ 10
# ⁠
# Sum: 15
#
# ⁠  10
# ⁠ /  \
# ⁠2    3
#
# Sum: 15
#
#
#
#
# Example 2:
#
# Input:
# ⁠   1
# ⁠  / \
# ⁠ 2  10
# ⁠   /  \
# ⁠  2   20
#
# Output: False
# Explanation: You can't split the tree into two trees with equal sum after
# removing exactly one edge on the tree.
#
#
#
# Note:
#
# The range of tree node value is in the range of [-100000, 100000].
# 1
#
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Solution:
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.s = collections.defaultdict(int)
        self.saveSum(root)
        return self.DFS(root, self.s[root])

    def saveSum(self, root):
        if root is None:
            return 0
        res = root.val + self.saveSum(root.left) + self.saveSum(root.right)
        self.s[root] = res
        return res

    def DFS(self, root, all):
        if root is None:
            return False
        if root.right is not None and all - self.s[root.right] == self.s[root.right]:
            return True
        if root.left is not None and all - self.s[root.left] == self.s[root.left]:
            return True
        return self.DFS(root.left, all) or self.DFS(root.right, all)
