#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (34.19%)
# Total Accepted:    110.9K
# Total Submissions: 324K
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# Given inorder and postorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
#
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
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
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        self.dic = {}
        for i in range(len(inorder)):
            self.dic[inorder[i]] = i
        return self.helper(inorder, postorder, 0, len(inorder)-1, 0, len(inorder)-1)

    def helper(self, inorder, postorder, l, r, a, b):
        if r-l+1 == 0:
            return None
        if l == r:
            return TreeNode(inorder[l])
        res = TreeNode(postorder[b])
        length = self.dic[postorder[b]] - l
        res.left = self.helper(inorder, postorder, l, l+length-1, a, a+length-1)
        res.right= self.helper(inorder, postorder, l+length+1, r, a+length, b-1)
        return res
