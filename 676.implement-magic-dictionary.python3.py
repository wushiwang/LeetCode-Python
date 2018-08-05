#
# [676] Implement Magic Dictionary
#
# https://leetcode.com/problems/implement-magic-dictionary/description/
#
# algorithms
# Medium (49.08%)
# Total Accepted:    14.7K
# Total Submissions: 30K
# Testcase Example:  '["MagicDictionary", "buildDict", "search", "search", "search", "search"]\n[[], [["hello","leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]'
#
#
# Implement a magic directory with buildDict, and search methods.
#
#
#
# For the method buildDict, you'll be given a list of non-repetitive words to
# build a dictionary.
#
#
#
# For the method search, you'll be given a word, and judge whether if you
# modify exactly one character into another character in this word, the
# modified word is in the dictionary you just built.
#
#
# Example 1:
#
# Input: buildDict(["hello", "leetcode"]), Output: Null
# Input: search("hello"), Output: False
# Input: search("hhllo"), Output: True
# Input: search("hell"), Output: False
# Input: search("leetcoded"), Output: False
#
#
#
# Note:
#
# You may assume that all the inputs are consist of lowercase letters a-z.
# For contest purpose, the test data is rather small by now. You could think
# about highly efficient algorithm after the contest.
# Please remember to RESET your class variables declared in class
# MagicDictionary, as static/class variables are persisted across multiple test
# cases. Please see here for more details.
#


class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = dict()

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: void
        """
        for word in dict:
            if len(word) not in self.dic:
                self.dic[len(word)] = []
            self.dic[len(word)].append(word)

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        if len(word) not in self.dic:
            return False
        return self._check(word, self.dic[len(word)])

    def _check(self, word, lst):
        for w in lst:
            cur = 0
            for i in range(len(w)):
                if w[i] != word[i]:
                    cur += 1
                if cur == 2:
                    break
            if cur == 1:
                return True
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
