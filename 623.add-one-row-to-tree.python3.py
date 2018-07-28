#
# [623] Add One Row to Tree
#
# https://leetcode.com/problems/add-one-row-to-tree/description/
#
# algorithms
# Medium (46.14%)
# Total Accepted:    17.5K
# Total Submissions: 37.8K
# Testcase Example:  '[4,2,6,3,1,5]\n1\n2'
#
# Given the root of a binary tree, then value v and depth d, you need to add a
# row of nodes with value v at the given depth d. The root node is at depth
# 1.
#
# The adding rule is: given a positive integer depth d, for each NOT null tree
# nodes N in depth d-1, create two tree nodes with value v as N's left subtree
# root and right subtree root. And N's original left subtree should be the left
# subtree of the new left subtree root, its original right subtree should be
# the right subtree of the new right subtree root. If depth d is 1 that means
# there is no depth d-1 at all, then create a tree node with value v as the new
# root of the whole original tree, and the original tree is the new root's left
# subtree.
#
# Example 1:
#
# Input:
# A binary tree as following:
# ⁠      4
# ⁠    /   \
# ⁠   2     6
# ⁠  / \   /
# ⁠ 3   1 5
#
# v = 1
#
# d = 2
#
# Output:
# ⁠      4
# ⁠     / \
# ⁠    1   1
# ⁠   /     \
# ⁠  2       6
# ⁠ / \     /
# ⁠3   1   5
#
#
#
#
#
# Example 2:
#
# Input:
# A binary tree as following:
# ⁠     4
# ⁠    /
# ⁠   2
# ⁠  / \
# ⁠ 3   1
#
# v = 1
#
# d = 3
#
# Output:
# ⁠     4
# ⁠    /
# ⁠   2
# ⁠  / \
# ⁠ 1   1
# ⁠/     \
# 3       1
#
#
#
# Note:
#
# The given d is in range [1, maximum depth of the given tree + 1].
# The given binary tree has at least one tree node.
#


class Solution:
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node
        self.DFS(root, v, d, 1)
        return root

    def DFS(self, root, v, d, level):
        if root is None:
            return
        if level == d-1:
            left, right = TreeNode(v), TreeNode(v)
            left.left = root.left
            right.right = root.right
            root.left, root.right = left, right
            return
        self.DFS(root.left, v, d, level+1)
        self.DFS(root.right, v, d, level+1)
