#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (43.16%)
# Total Accepted:    246.5K
# Total Submissions: 570.9K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
#
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
#
# return its level order traversal as:
#
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
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
import collections


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        que, res = collections.deque(), []
        que.append((root, 0))
        while len(que) != 0:
            cur = que.popleft()
            if cur[1] >= len(res):
                res.append([])
            res[cur[1]].append(cur[0].val)
            if cur[0].left is not None:
                que.append((cur[0].left, cur[1]+1))
            if cur[0].right is not None:
                que.append((cur[0].right, cur[1]+1))
        return res
