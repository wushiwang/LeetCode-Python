#
# [677] Map Sum Pairs
#
# https://leetcode.com/problems/map-sum-pairs/description/
#
# algorithms
# Medium (50.74%)
# Total Accepted:    15.3K
# Total Submissions: 30.1K
# Testcase Example:  '["MapSum", "insert", "sum", "insert", "sum"]\n[[], ["apple",3], ["ap"], ["app",2], ["ap"]]'
#
#
# Implement a MapSum class with insert, and sum methods.
#
#
#
# For the method insert, you'll be given a pair of (string, integer). The
# string represents the key and the integer represents the value. If the key
# already existed, then the original key-value pair will be overridden to the
# new one.
#
#
#
# For the method sum, you'll be given a string representing the prefix, and you
# need to return the sum of all the pairs' value whose key starts with the
# prefix.
#
#
# Example 1:
#
# Input: insert("apple", 3), Output: Null
# Input: sum("ap"), Output: 3
# Input: insert("app", 2), Output: Null
# Input: sum("ap"), Output: 5
#
#
#
#
class MapSum:
    class Trie:
        class TrieNode:
            def __init__(self):
                self.val = None
                self.chd = [None]*26

        def __init__(self):
            self.root = self.TrieNode()

        def ctoi(self, c):
            return ord(c) - ord('a')

        def insert(self, word, val):
            root, i = self.root, 0
            while i < len(word):
                cur = self.ctoi(word[i])
                if root.chd[cur] is None:
                    root.chd[cur] = self.TrieNode()
                root = root.chd[cur]
                i += 1
            root.val = val

        def sum(self, pre):
            root, i = self.root, 0
            # Find node
            while i < len(pre) and root is not None:
                cur = self.ctoi(pre[i])
                root = root.chd[cur]
                i += 1
            return self._getSum(root)

        def _getSum(self, node):
            if node is None:
                return 0
            res = 0
            if node.val is not None:
                res += node.val
            for i in range(26):
                res += self._getSum(node.chd[i])
            return res


    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = self.Trie()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.trie.insert(key, val)

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        return self.trie.sum(prefix)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
