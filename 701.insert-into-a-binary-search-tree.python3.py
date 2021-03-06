#
# [784] Insert into a Binary Search Tree
#
# https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
#
# algorithms
# Medium (46.81%)
# Total Accepted:    2.7K
# Total Submissions: 5.7K
# Testcase Example:  '[4,2,7,1,3]\n5'
#
# Given the root node of a binary search tree (BST) and a value to be inserted
# into the tree, insert the value into the BST. Return the root node of the BST
# after the insertion. It is guaranteed that the new value does not exist in
# the original BST.
#
# Note that there may exist multiple valid ways for the insertion, as long as
# the tree remains a BST after insertion. You can return any of them.
#
# For example, 
#
#
# Given the tree:
# ⁠       4
# ⁠      / \
# ⁠     2   7
# ⁠    / \
# ⁠   1   3
# And the value to insert: 5
#
#
# You can return this binary search tree:
#
#
# ⁠        4
# ⁠      /   \
# ⁠     2     7
# ⁠    / \   /
# ⁠   1   3 5
#
#
# This tree is also valid:
#
#
# ⁠        5
# ⁠      /   \
# ⁠     2     7
# ⁠    / \
# ⁠   1   3
# ⁠        \
# ⁠         4
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return
        if val > root.val:
            if root.right is None:
                root.right = TreeNode(val)
            else:
                self.insertIntoBST(root.right, val)
        else:
            if root.left is None:
                root.left = TreeNode(val)
            else:
                self.insertIntoBST(root.left, val)
        return root
