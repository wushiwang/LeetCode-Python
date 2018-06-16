#
# [211] Add and Search Word - Data structure design
#
# https://leetcode.com/problems/add-and-search-word-data-structure-design/description/
#
# algorithms
# Medium (25.85%)
# Total Accepted:    78.8K
# Total Submissions: 304.2K
# Testcase Example:  '["WordDictionary","addWord","addWord","addWord","search",
# "search","search","search"]\n[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]'
#
# Design a data structure that supports the following two operations:
#
#
# void addWord(word)
# bool search(word)
#
#
# search(word) can search a literal word or a regular expression string
# containing only letters a-z or .. A . means it can represent any one letter.
#
# Example:
#
#
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
#
#
# Note:
# You may assume that all words are consist of lowercase letters a-z.
#


class WordDictionary:

    # Trie Tree Node
    class Node:

        def __init__(self):
            self.isWord = False
            self.chd = dict()

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = self.Node()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        head = self.head
        for c in word:
            if c not in head.chd:
                head.chd[c] = self.Node()
            head = head.chd[c]
        head.isWord = True

    def search(self, word, head=None):
        """
        Returns if the word is in the data structure.
        A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if head is None:
            head = self.head
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                for k in head.chd:
                    if self.search(word[i+1:], head.chd[k]):
                        return True
                return False
            else:
                if c not in head.chd:
                    return False
                head = head.chd[c]
        return head.isWord

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
