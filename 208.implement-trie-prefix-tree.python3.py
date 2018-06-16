#
# [208] Implement Trie (Prefix Tree)
#
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (31.58%)
# Total Accepted:    117.2K
# Total Submissions: 370.2K
# Testcase Example:  '["Trie","insert","search","search","startsWith",
# "insert","search"]\n[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# Implement a trie with insert, search, and startsWith methods.
#
# Example:
#
#
# Trie trie = new Trie();
#
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");
# trie.search("app");     // returns true
#
#
# Note:
#
#
# You may assume that all inputs are consist of lowercase letters a-z.
# All inputs are guaranteed to be non-empty strings.
#


class Trie:

    class Node:

        def __init__(self):
            self.chd = dict()
            self.isWord = False

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = self.Node()
        self.base = ord('a')

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        head = self.head
        for c in word:
            pos = ord(c) - self.base
            if pos not in head.chd:
                head.chd[pos] = self.Node()
            head = head.chd[pos]
        head.isWord = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        head = self.head
        for c in word:
            pos = ord(c) - self.base
            if pos not in head.chd:
                return False
            head = head.chd[pos]
        return head.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the
        given prefix.
        :type prefix: str
        :rtype: bool
        """
        head = self.head
        for c in prefix:
            pos = ord(c) - self.base
            if pos not in head.chd:
                return False
            head = head.chd[pos]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
