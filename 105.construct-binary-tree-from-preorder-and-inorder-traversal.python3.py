#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (34.81%)
# Total Accepted:    145K
# Total Submissions: 416.3K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
#
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
#
# Return the following binary tree:
#
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.dic = {}
        for i in range(len(inorder)):
            self.dic[inorder[i]] = i
        return self.helper(preorder, inorder, 0, len(preorder)-1, 0, len(preorder)-1)

    def helper(self, preorder, inorder, l, r, a, b):
        if r-l+1 == 0:
            return None

        if l == r:
            return TreeNode(preorder[l])

        res = TreeNode(preorder[l])
        length = self.dic[preorder[l]] - a
        res.left = self.helper(preorder, inorder, l+1, l+length, a, b+length-1)
        res.right = self.helper(preorder, inorder, l+length+1, r, a+length+1, b)
        return res
