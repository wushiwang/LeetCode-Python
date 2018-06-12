#
# [145] Binary Tree Postorder Traversal
#
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (42.93%)
# Total Accepted:    185.9K
# Total Submissions: 432.3K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the postorder traversal of its nodes' values.
#
# Example:
#
#
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
#
# Output: [3,2,1]
#
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack, res = [root], []
        while len(stack) != 0:
            top = stack.pop()
            if type(top) is int:
                res.append(top)
                continue
            if top is not None:
                stack.append(top.val)
                stack.append(top.right)
                stack.append(top.left)
        return res
