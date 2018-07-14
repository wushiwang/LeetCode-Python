#
# [450] Delete Node in a BST
#
# https://leetcode.com/problems/delete-node-in-a-bst/description/
#
# algorithms
# Medium (37.54%)
# Total Accepted:    37.8K
# Total Submissions: 100.6K
# Testcase Example:  '[5,3,6,2,4,null,7]\n3'
#
# Given a root node reference of a BST and a key, delete the node with the
# given key in the BST. Return the root node reference (possibly updated) of
# the BST.
#
# Basically, the deletion can be divided into two stages:
#
# Search for a node to remove.
# If the node is found, delete the node.
#
#
#
# Note: Time complexity should be O(height of tree).
#
# Example:
#
# root = [5,3,6,2,4,null,7]
# key = 3
#
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
#
# Given key to delete is 3. So we find the node with value 3 and delete it.
#
# One valid answer is [5,4,6,2,null,null,7], shown in the following BST.
#
# ⁠   5
# ⁠  / \
# ⁠ 4   6
# ⁠/     \
# 2       7
#
# Another valid answer is [5,2,6,null,4,null,7].
#
# ⁠   5
# ⁠  / \
# ⁠ 2   6
# ⁠  \   \
# ⁠   4   7
#
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
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        dum = TreeNode(None)
        dum.left = root
        self.pre = dum
        res = self.find(root, key)
        if res is None:
            return root
        if res.left is None and res.right is None:
            self.delete(res, None)
        elif res.right is None:
            self.delete(res, res.left)
        elif res.left is None:
            self.delete(res, res.right)
        else:
            pos = self.findNextPre(res.right)
            res.val = pos.val
            pos.val = -math.inf
            res.right = self.deleteNode(res.right, -math.inf)
        return dum.left

    def find(self, root, key):
        if root is None:
            return
        if root.val == key:
            return root
        self.pre = root
        if key < root.val:
            return self.find(root.left, key)
        else:
            return self.find(root.right, key)

    def findNextPre(self, root):
        if root is None:
            return None
        self.fa = None
        while root.left is not None:
            self.fa = root
            root = root.left
        return root

    def delete(self, key, v):
        if self.pre.left == key:
            self.pre.left = v
        else:
            self.pre.right = v
