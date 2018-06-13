#
# [156] Binary Tree Upside Down
#
# https://leetcode.com/problems/binary-tree-upside-down/description/
#
# algorithms
# Medium (46.45%)
# Total Accepted:    36.1K
# Total Submissions: 77.7K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given a binary tree where all the right nodes are either leaf nodes with a
# sibling (a left node that shares the same parent node) or empty, flip it
# upside down and turn it into a tree where the original right nodes turned
# into left leaf nodes. Return the new root.
#
# Example:
#
#
# Input: [1,2,3,4,5]
#
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# ⁠/ \
# 4   5
#
# Output: return the root of the binary tree [4,5,2,#,#,3,1]
#
# ⁠  4
# ⁠ / \
# ⁠5   2
# ⁠   / \
# ⁠  3   1
#
#
# Clarification:
#
# Confused what [4,5,2,#,#,3,1] means? Read more below on how binary tree is
# serialized on OJ.
#
# The serialization of a binary tree follows a level order traversal, where '#'
# signifies a path terminator where no node exists below.
#
# Here's an example:
#
#
# ⁠  1
# ⁠ / \
# ⁠2   3
# ⁠   /
# ⁠  4
# ⁠   \
# ⁠    5
#
#
# The above binary tree is serialized as [1,2,3,#,#,4,#,#,5].
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return
        nroot = TreeNode(root.val)
        return self.DFS(root, nroot)

    def DFS(self, root, res):
        if root.left is None:
            return res
        else:
            if root.right is None:
                nroot = TreeNode(root.left.val)
                nroot.right = res
                return self.DFS(root.left, nroot)
            else:
                nroot, nleft = TreeNode(root.left.val), TreeNode(root.right.val)
                nroot.left, nroot.right = nleft, res
                return self.DFS(root.left, nroot)
