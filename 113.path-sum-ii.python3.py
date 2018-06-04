#
# [113] Path Sum II
#
# https://leetcode.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (36.17%)
# Total Accepted:    168.1K
# Total Submissions: 464.6K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# Given a binary tree and a sum, find all root-to-leaf paths where each path's
# sum equals the given sum.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given the below binary tree and sum = 22,
#
#
# ⁠     5
# ⁠    / \
# ⁠   4   8
# ⁠  /   / \
# ⁠ 11  13  4
# ⁠/  \    / \
# 7    2  5   1
#
#
# Return:
#
#
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
# ]
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
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        self.helper(root, sum, [], res)
        return res

    def helper(self, root, sum, cur, res):
        if root is None:
            return
        if root.left is None and root.right is None:
            if sum == root.val:
                res.append(cur+[root.val])
            return
        if root.left is not None:
            self.helper(root.left, sum-root.val, cur+[root.val], res)
        if root.right is not None:
            self.helper(root.right, sum-root.val, cur+[root.val], res)
