#
# [255] Verify Preorder Sequence in Binary Search Tree
#
# https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/description/
#
# algorithms
# Medium (41.18%)
# Total Accepted:    26.1K
# Total Submissions: 63.3K
# Testcase Example:  '[5,2,6,1,3]'
#
# Given an array of numbers, verify whether it is the correct preorder
# traversal sequence of a binary search tree.
#
# You may assume each number in the sequence is unique.
#
# Consider the following binary search tree: 
#
#
# ⁠    5
# ⁠   / \
# ⁠  2   6
# ⁠ / \
# ⁠1   3
#
# Example 1:
#
#
# Input: [5,2,6,1,3]
# Output: false
#
# Example 2:
#
#
# Input: [5,2,1,3,6]
# Output: true
#
# Follow up:
# Could you do it using only constant space complexity?
#
# 1 2 3 5 6


class Solution:
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        self.dic = {y:x for x, y in enumerate(sorted(preorder))}
        return self.check(preorder, 0, len(preorder), 0, len(preorder))

    def check(self, preorder, A, B, L, R):
        if B-A == 0:
            return True
        pos = self.dic[preorder[A]]
        if pos >= L and pos < R:
            return self.check(preorder, A+1, pos-L+A+1, L, pos) and\
                self.check(preorder, pos-L+A+1, B, pos+1, R)
        else:
            return False
