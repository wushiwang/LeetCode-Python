#
# [572] Subtree of Another Tree
#
# https://leetcode.com/problems/subtree-of-another-tree/description/
#
# algorithms
# Easy (40.29%)
# Total Accepted:    56.3K
# Total Submissions: 139.8K
# Testcase Example:  '[3,4,5,1,2]\n[4,1,2]'
#
#
# Given two non-empty binary trees s and t, check whether tree t has exactly
# the same structure and node values with a subtree of s. A subtree of s is a
# tree consists of a node in s and all of this node's descendants. The tree s
# could also be considered as a subtree of itself.
#
#
# Example 1:
#
# Given tree s:
#
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
#
# Given tree t:
#
# ⁠  4
# ⁠ / \
# ⁠1   2
#
# Return true, because t has the same structure and node values with a subtree
# of s.
#
#
# Example 2:
#
# Given tree s:
#
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
# ⁠   /
# ⁠  0
#
# Given tree t:
#
# ⁠  4
# ⁠ / \
# ⁠1   2
#
# Return false.
#


class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s is None:
            return False
        if self.same(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def same(self, a, b):
        if a is None and b is None:
            return True
        elif a is not None and b is not None:
            return a.val == b.val and self.same(a.left, b.left) and self.same(a.right, b.right)
        else:
            return False
