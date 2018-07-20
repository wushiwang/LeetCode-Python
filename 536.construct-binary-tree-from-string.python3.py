#
# [536] Construct Binary Tree from String
#
# https://leetcode.com/problems/construct-binary-tree-from-string/description/
#
# algorithms
# Medium (42.73%)
# Total Accepted:    12.3K
# Total Submissions: 28.9K
# Testcase Example:  '"4(2(3)(1))(6(5))"'
#
# You need to construct a binary tree from a string consisting of parenthesis
# and integers.
#
# The whole input represents a binary tree. It contains an integer followed by
# zero, one or two pairs of parenthesis. The integer represents the root's
# value and a pair of parenthesis contains a child binary tree with the same
# structure.
#
# You always start to construct the left child node of the parent first if it
# exists.
#
# Example:
#
# Input: "4(2(3)(1))(6(5))"
# Output: return the tree root node representing the following tree:
#
# ⁠      4
# ⁠    /   \
# ⁠   2     6
# ⁠  / \   /
# ⁠ 3   1 5
#
#
#
# Note:
#
# There will only be '(',  ')',  '-' and  '0' ~ '9' in the input string.
# An empty tree is represented by "" instead of "()".
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
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        root, pos = self.helper(s, 0)
        return root

# Input: "4(2(3)(1))(6(5))"
    def helper(self, s, pos):
        if pos == len(s):
            return None, pos
        i = pos
        while i < len(s) and s[i] != '(' and s[i] != ')':
            i += 1
        n = int(s[pos:i])
        node = TreeNode(n)
        if i < len(s) and s[i] == '(':
            node.left, i = self.helper(s, i+1)
            i += 1
            if i< len(s) and s[i] == '(':
                node.right, i = self.helper(s, i+1)
                i += 1
        return node, i
