#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (37.21%)
# Total Accepted:    141.6K
# Total Submissions: 380.4K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the zigzag level order traversal of its nodes'
# values. (ie, from left to right, then right to left for the next level and
# alternate between).
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
# return its zigzag level order traversal as:
#
# [
# ⁠ [3],
# ⁠ [20,9],
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        res = []
        que = collections.deque()
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
        for i in range(len(res)):
            if i & 1 == 1:
                res[i] = res[i][::-1]

        return res
