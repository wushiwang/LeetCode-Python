#
# [449] Serialize and Deserialize BST
#
# https://leetcode.com/problems/serialize-and-deserialize-bst/description/
#
# algorithms
# Medium (42.80%)
# Total Accepted:    30.5K
# Total Submissions: 71.4K
# Testcase Example:  '[2,1,3]'
#
# Serialization is the process of converting a data structure or object into a
# sequence of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary search tree. There
# is no restriction on how your serialization/deserialization algorithm should
# work. You just need to ensure that a binary search tree can be serialized to
# a string and this string can be deserialized to the original tree
# structure.
#
#
# The encoded string should be as compact as possible.
#
#
#
# Note: Do not use class member/global/static variables to store states. Your
# serialize and deserialize algorithms should be stateless.
#
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """
        Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        # pre-order traveling
        self.res = ""
        self.pre(root)
        return self.res[:-1]

    def pre(self, root):
        if root is None:
            return
        self.res += (str(root.val)+' ')
        self.pre(root.left)
        self.pre(root.right)

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        self.data = list(map(int, data.split(' ')))
        self.pos = 0
        return self.helper(float('-inf'), float('inf'))

    def helper(self, min, max):
        if self.pos < len(self.data):
            cur = self.data[self.pos]
        else:
            return None
        self.pos += 1
        if cur < min or cur > max:
            self.pos -= 1
            return None
        root = TreeNode(cur)
        root.left = self.helper(min, cur)
        root.right = self.helper(cur, max)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
