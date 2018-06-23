#
# [270] Closest Binary Search Tree Value
#
# https://leetcode.com/problems/closest-binary-search-tree-value/description/
#
# algorithms
# Easy (41.02%)
# Total Accepted:    55.6K
# Total Submissions: 135.7K
# Testcase Example:  '[4,2,5,1,3]\n3.714286'
#
# Given a non-empty binary search tree and a target value, find the value in
# the BST that is closest to the target.
#
# Note:
#
#
# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest
# to the target.
#
#
# Example:
#
#
# Input: root = [4,2,5,1,3], target = 3.714286
#
# ⁠   4
# ⁠  / \
# ⁠ 2   5
# ⁠/ \
# 1   3
#
# Output: 4
#
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if root is None:
            return
        res = [abs(root.val - target), root.val]
        self.DFS(root, target, res)
        return res[1]

    def DFS(self, root, target, res):
        if root is None:
            return
        if abs(root.val - target) < res[0]:
            res[0], res[1] = abs(root.val - target), root.val
        if root.left is not None and target < root.val:
            self.DFS(root.left, target, res)
        if root.right is not None and target > root.val:
            self.DFS(root.right, target, res)
