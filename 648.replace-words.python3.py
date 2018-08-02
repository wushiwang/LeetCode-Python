#
# [648] Replace Words
#
# https://leetcode.com/problems/replace-words/description/
#
# algorithms
# Medium (48.54%)
# Total Accepted:    20.7K
# Total Submissions: 42.7K
# Testcase Example:  '["cat", "bat", "rat"]\n"the cattle was rattled by the battery"'
#
#
# In English, we have a concept called root, which can be followed by some
# other words to form another longer word - let's call this word successor. For
# example, the root an, followed by other, which can form another word
# another.
#
#
#
#
# Now, given a dictionary consisting of many roots and a sentence. You need to
# replace all the successor in the sentence with the root forming it. If a
# successor has many roots can form it, replace it with the root with the
# shortest length.
#
#
#
# You need to output the sentence after the replacement.
#
#
#
# Example 1:
#
# Input: dict = ["cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"
#
#
#
#
# Note:
#
# The input will only have lower-case letters.
# ⁠1
# ⁠1
# ⁠1
# ⁠1
#


class Solution:
    class Trie:
        class TrieNode:
            def __init__(self):
                self.chd = [None]*26
                self.isRoot = False

        def __init__(self):
            self.root = self.TrieNode()

        def ctoi(self, c):
            return ord(c) - ord('a')

        def add(self, word):
            pos, node = 0, self.root
            while pos < len(word):
                if node.chd[self.ctoi(word[pos])] is None:
                    node.chd[self.ctoi(word[pos])] = self.TrieNode()
                node = node.chd[self.ctoi(word[pos])]
                pos += 1
            node.isRoot = True

        def check(self, word):
            pos, node = 0, self.root
            while pos < len(word):
                node = node.chd[self.ctoi(word[pos])]
                if node is None:
                    return False, ''
                elif node.isRoot:
                    return True, word[:pos+1]
                pos += 1
            return False, ''


    def replaceWords(self, dic, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = self.Trie()
        for root in dic:
            trie.add(root)
        lst = sentence.split(' ')
        res = []
        for word in lst:
            c, v = trie.check(word)
            if c:
                res.append(v)
            else:
                res.append(word)
        return ' '.join(res)
