#
# [642] Design Search Autocomplete System
#
# https://leetcode.com/problems/design-search-autocomplete-system/description/
#
# algorithms
# Hard (30.69%)
# Total Accepted:    7.6K
# Total Submissions: 24.8K
# Testcase Example:  '["AutocompleteSystem","input","input","input","input"]\n
# [[["i love you","island","iroman","i love leetcode"],[5,3,2,2]],["i"],[" "],
# ["a"],["#"]]'
#
# Design a search autocomplete system for a search engine. Users may input a
# sentence (at least one word and end with a special character '#'). For each
# character they type except '#', you need to return the top 3 historical hot
# sentences that have prefix the same as the part of sentence already typed.
# Here are the specific rules:
#
# The hot degree for a sentence is defined as the number of times a user typed
# the exactly same sentence before.
# The returned top 3 hot sentences should be sorted by hot degree (The first is
# the hottest one). If several sentences have the same degree of hot, you need
# to use ASCII-code order (smaller one appears first).
# If less than 3 hot sentences exist, then just return as many as you can.
# When the input is a special character, it means the sentence ends, and in
# this case, you need to return an empty list.
#
#
# Your job is to implement the following functions:
#
# The constructor function:
#
# AutocompleteSystem(String[] sentences, int[] times): This is the constructor.
# The input is historical data. Sentences is a string array consists of
# previously typed sentences. Times is the corresponding times a sentence has
# been typed. Your system should record these historical data.
#
# Now, the user wants to input a new sentence. The following function will
# provide the next character the user types:
#
# List<String> input(char c): The input c is the next character typed by the
# user. The character will only be lower-case letters ('a' to 'z'), blank space
# (' ') or a special character ('#'). Also, the previously typed sentence
# should be recorded in your system. The output will be the top 3 historical
# hot sentences that have prefix the same as the part of sentence already
# typed.
#
#
# Example:
#
# Operation: AutocompleteSystem(["i love you", "island","ironman", "i love
# leetcode"], [5,3,2,2])
#
# The system have already tracked down the following sentences and their
# corresponding times:
#
# "i love you" : 5 times
#
# "island" : 3 times
#
# "ironman" : 2 times
#
# "i love leetcode" : 2 times
#
# Now, the user begins another search:
#
# Operation: input('i')
#
# Output: ["i love you", "island","i love leetcode"]
#
# Explanation:
#
# There are four sentences that have prefix "i". Among them, "ironman" and "i
# love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has
# ASCII code 114, "i love leetcode" should be in front of "ironman". Also we
# only need to output top 3 hot sentences, so "ironman" will be ignored.
#
# Operation: input(' ')
#
# Output: ["i love you","i love leetcode"]
#
# Explanation:
#
# There are only two sentences that have prefix "i ".
#
# Operation: input('a')
#
# Output: []
#
# Explanation:
#
# There are no sentences that have prefix "i a".
#
# Operation: input('#')
#
# Output: []
#
# Explanation:
#
# The user finished the input, the sentence "i a" should be saved as a
# historical sentence in system. And the following input will be counted as a
# new search.
#
#
#
#
# Note:
#
#
#
# The input sentence will always start with a letter and end with '#', and only
# one blank space will exist between two words.
# The number of complete sentences that to be searched won't exceed 100. The
# length of each sentence including those in the historical data won't exceed
# 100.
# Please use double-quote instead of single-quote when you write test cases
# even for a character input.
# Please remember to RESET your class variables declared in class
# AutocompleteSystem, as static/class variables are persisted across multiple
# test cases. Please see here for more details.
#
import math


class AutocompleteSystem:
    class Trie:
        class TrieNode:
            def __init__(self):
                self.chd = [None]*27
                self.sentences = set()

        def __init__(self):
            self.root = self.TrieNode()

        def ctoi(self, c):
            if c != ' ':
                return ord(c) - ord('a')
            else:
                return 26

        def add(self, s):
            root, i = self.root, 0
            while i < len(s):
                root.sentences.add(s)
                pos = self.ctoi(s[i])
                if root.chd[pos] is None:
                    root.chd[pos] = self.TrieNode()
                root = root.chd[pos]
                i += 1
            root.sentences.add(s)

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.trie = self.Trie()
        self.dic = dict()
        for i in range(len(sentences)):
            self.trie.add(sentences[i])
            self.dic[sentences[i]] = times[i]
        self.cur = ''
        self.node = self.trie.root

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == '#':
            if self.cur not in self.dic:
                self.dic[self.cur] = 0
            self.dic[self.cur] += 1
            self.trie.add(self.cur)
            self.cur = ''
            self.node = self.trie.root
            return []
        else:
            self.cur += c
            pos = self.trie.ctoi(c)
            if self.node is None or self.node.chd[pos] is None:
                return []
            else:
                self.node = self.node.chd[pos]
            max1 = max2 = max3 = -math.inf
            res1 = res2 = res3 = None
            for k in self.node.sentences:
                v = self.dic[k]
                if k.find(self.cur) == 0:
                    if v > max1 or (v == max1 and k < res1):
                        max3, res3 = max2, res2
                        max2, res2 = max1, res1
                        max1, res1 = v, k
                    elif v > max2 or (v == max2 and k < res2):
                        max3, res3 = max2, res2
                        max2, res2 = v, k
                    elif v > max3 or (v == max3 and k < res3):
                        max3, res3 = v, k
            res = []
            if max1 != -math.inf:
                res.append(res1)
            if max2 != -math.inf:
                res.append(res2)
            if max3 != -math.inf:
                res.append(res3)
            return res


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
