#
# [366] Find Leaves of Binary Tree
#
# https://leetcode.com/problems/find-leaves-of-binary-tree/description/
#
# algorithms
# Medium (61.50%)
# Total Accepted:    28.3K
# Total Submissions: 46K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given a binary tree, collect a tree's nodes as if you were doing this:
# Collect and remove all leaves, repeat until the tree is empty.
#
#
#
# Example:
# Given binary tree
#
# ⁠         1
# ⁠        / \
# ⁠       2   3
# ⁠      / \
# ⁠     4   5
#
#
#
# Returns [4, 5, 3], [2], [1].
#
#
#
# Explanation:
#
# 1. Removing the leaves [4, 5, 3] would result in this tree:
#
# ⁠         1
# ⁠        /
# ⁠       2
#
#
#
# 2. Now removing the leaf [2] would result in this tree:
#
# ⁠         1
#
#
#
# 3. Now removing the leaf [1] would result in the empty tree:
#
# ⁠         []
#
#
#
#
# Returns [4, 5, 3], [2], [1].
#
#
# Credits:Special thanks to @elmirap for adding this problem and creating all
# test cases.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.DFS(root, res)
        return res

    def DFS(self, root, res):
        if root is None:
            return -1
        # Check leaf
        if root.left is None and root.right is None:
            if len(res) == 0:
                res.append([])
            res[0].append(root.val)
            return 1

        cur = max(self.DFS(root.left, res), self.DFS(root.right, res))
        if len(res) < cur+1:
            res.append([])
        res[cur].append(root.val)
        return cur+1
