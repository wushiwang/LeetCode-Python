#
# [538] Convert BST to Greater Tree
#
# https://leetcode.com/problems/convert-bst-to-greater-tree/description/
#
# algorithms
# Easy (48.67%)
# Total Accepted:    49.1K
# Total Submissions: 100.9K
# Testcase Example:  '[5,2,13]'
#
# Given a Binary Search Tree (BST), convert it to a Greater Tree such that
# every key of the original BST is changed to the original key plus sum of all
# keys greater than the original key in BST.
#
#
# Example:
#
# Input: The root of a Binary Search Tree like this:
# ⁠             5
# ⁠           /   \
# ⁠          2     13
#
# Output: The root of a Greater Tree like this:
# ⁠            18
# ⁠           /   \
# ⁠         20     13
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
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.DFS(root, 0)

    def DFS(self, root, cur):
        if root is None:
            return None
        s = self.sum(root.right)
        node = TreeNode(root.val+s+cur)
        node.left = self.DFS(root.left, cur+root.val+s)
        node.right = self.DFS(root.right, cur)
        return node

    def sum(self, root):
        if root is None:
            return 0
        return root.val + self.sum(root.left) + self.sum(root.right)
