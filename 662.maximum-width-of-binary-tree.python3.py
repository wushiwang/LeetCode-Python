#
# [662] Maximum Width of Binary Tree
#
# https://leetcode.com/problems/maximum-width-of-binary-tree/description/
#
# algorithms
# Medium (38.36%)
# Total Accepted:    17.3K
# Total Submissions: 45.1K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# Given a binary tree, write a function to get the maximum width of the given
# tree. The width of a tree is the maximum width among all levels. The binary
# tree has the same structure as a full binary tree, but some nodes are null.
#
# The width of one level is defined as the length between the end-nodes (the
# leftmost and right most non-null nodes in the level, where the null nodes
# between the end-nodes are also counted into the length calculation.
#
# Example 1:
#
# Input:
#
# ⁠          1
# ⁠        /   \
# ⁠       3     2
# ⁠      / \     \
# ⁠     5   3     9
#
# Output: 4
# Explanation: The maximum width existing in the third level with the length 4
# (5,3,null,9).
#
#
#
# Example 2:
#
# Input:
#
# ⁠         1
# ⁠        /
# ⁠       3
# ⁠      / \
# ⁠     5   3
#
# Output: 2
# Explanation: The maximum width existing in the third level with the length 2
# (5,3).
#
#
#
# Example 3:
#
# Input:
#
# ⁠         1
# ⁠        / \
# ⁠       3   2
# ⁠      /
# ⁠     5
#
# Output: 2
# Explanation: The maximum width existing in the second level with the length 2
# (3,2).
#
#
# Example 4:
#
# Input:
#
# ⁠         1
# ⁠        / \
# ⁠       3   2
# ⁠      /     \
# ⁠     5       9
# ⁠    /         \
# ⁠   6           7
# Output: 8
# Explanation:The maximum width existing in the fourth level with the length 8
# (6,null,null,null,null,null,null,7).
#
#
#
#
# Note:
# Answer will in the range of 32-bit signed integer.
#
import math


class Solution:
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = []
        self.DFS(root, 0, 0)
        ans = 0
        for i in range(len(self.res)):
            ans =  max(ans, self.res[i][1] - self.res[i][0] + 1)
        return ans

    def DFS(self, root, level, n):
        if root is None:
            return
        if level == len(self.res):
            self.res.append([math.inf, -math.inf])
        self.res[level][0] = min(self.res[level][0], n)
        self.res[level][1] = max(self.res[level][1], n)
        self.DFS(root.left, level+1, n*2+1)
        self.DFS(root.right, level+1, n*2+2)
