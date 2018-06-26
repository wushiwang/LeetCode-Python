#
# [297] Serialize and Deserialize Binary Tree
#
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
#
# algorithms
# Hard (35.54%)
# Total Accepted:    110K
# Total Submissions: 309.6K
# Testcase Example:  '[1,2,3,null,null,4,5]'
#
# Serialization is the process of converting a data structure or object into a
# sequence of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary tree. There is no
# restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string and
# this string can be deserialized to the original tree structure.
#
# Example: 
#
#
# You may serialize the following tree:
#
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# ⁠    / \
# ⁠   4   5
#
# as "[1,2,3,null,null,4,5]"
#
#
# Clarification: The above format is the same as how LeetCode serializes a
# binary tree. You do not necessarily need to follow this format, so please be
# creative and come up with different approaches yourself.
#
# Note: Do not use class member/global/static variables to store states. Your
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
        # Serialize BST binary tree using inorder and preorder
        inorder, preorder = [], []
        self._id = 0
        self._dic = dict()
        self._inorder(root, inorder)
        self._preorder(root, preorder)
        inorder = ','.join(inorder)
        preorder = ','.join(preorder)
        return inorder+'#'+preorder

    def _inorder(self, root, res):
        if root is None:
            return
        self._inorder(root.left, res)
        res.append(str(root.val)+'$'+str(self._id))
        self._dic[root] = self._id
        self._id += 1
        self._inorder(root.right, res)

    def _preorder(self, root, res):
        if root is None:
            return
        res.append(str(root.val)+'$'+str(self._dic[root]))
        self._id += 1
        self._preorder(root.left, res)
        self._preorder(root.right, res)

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        print(data)
        # Get inorder and preorder list
        inorder, preorder = data.split('#')
        if inorder == '' or preorder == '':
            return None
        inorder = list(map(lambda x: x.split('$'), inorder.split(',')))
        preorder = list(map(lambda x: x.split('$'), preorder.split(',')))
        inorder = list(map(lambda x: (int(x[0]), int(x[1])), inorder))
        preorder = list(map(lambda x: (int(x[0]), int(x[1])), preorder))

        # Construct Binary Tree by inorder and preorder list
        dic = dict()
        for i in range(len(inorder)):
            dic[inorder[i]] = i
        res = self._helper(preorder, dic, 0)
        return res

    def _helper(self, preorder, dic, offset):
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0][0])
        node = TreeNode(preorder[0][0])
        length = dic[preorder[0]] - offset
        node.left = self._helper(preorder[1:length+1], dic, offset)
        node.right = self._helper(preorder[length+1:], dic, offset+length+1)
        return node

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
