#
# [655] Print Binary Tree
#
# https://leetcode.com/problems/print-binary-tree/description/
#
# algorithms
# Medium (48.92%)
# Total Accepted:    10.9K
# Total Submissions: 22.4K
# Testcase Example:  '[1,2]'
#
# Print a binary tree in an m*n 2D string array following these rules:
#
#
# The row number m should be equal to the height of the given binary tree.
# The column number n should always be an odd number.
# The root node's value (in string format) should be put in the exactly middle
# of the first row it can be put. The column and the row where the root node
# belongs will separate the rest space into two parts (left-bottom part and
# right-bottom part). You should print the left subtree in the left-bottom part
# and print the right subtree in the right-bottom part. The left-bottom part
# and the right-bottom part should have the same size. Even if one subtree is
# none while the other is not, you don't need to print anything for the none
# subtree but still need to leave the space as large as that for the other
# subtree. However, if two subtrees are none, then you don't need to leave
# space for both of them.
# Each unused space should contain an empty string "".
# Print the subtrees following the same rules.
#
#
# Example 1:
#
# Input:
# ⁠    1
# ⁠   /
# ⁠  2
# Output:
# [["", "1", ""],
# ⁠["2", "", ""]]
#
#
#
#
# Example 2:
#
# Input:
# ⁠    1
# ⁠   / \
# ⁠  2   3
# ⁠   \
# ⁠    4
# Output:
# [["", "", "", "1", "", "", ""],
# ⁠["", "2", "", "", "", "3", ""],
# ⁠["", "", "4", "", "", "", ""]]
#
#
#
# Example 3:
#
# Input:
# ⁠     1
# ⁠    / \
# ⁠   2   5
# ⁠  /
# ⁠ 3
# ⁠/
# 4
# Output:
#
# [["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
# ⁠["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
# ⁠["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
# ⁠["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
#
#
#
# Note:
# The height of binary tree is in the range of [1, 10].
#


class Solution:
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        depth = self.getDepth(root)
        width = (2**depth) - 1
        self.res = [['']*width for _ in range(depth)]
        self.DFS(root, 0, width-1, 0)
        return self.res

    def DFS(self, root, L, R, level):
        if root is not None:
            mid = (L+R) >> 1
            self.res[level][mid] = str(root.val)
            self.DFS(root.left, L, mid-1, level+1)
            self.DFS(root.right, mid+1, R, level+1)

    def getDepth(self, root):
        if root is None:
            return 0
        return max(self.getDepth(root.left), self.getDepth(root.right)) + 1
