#
# [288] Unique Word Abbreviation
#
# https://leetcode.com/problems/unique-word-abbreviation/description/
#
# algorithms
# Medium (18.25%)
# Total Accepted:    33.6K
# Total Submissions: 184.4K
# Testcase Example:  '["ValidWordAbbr","isUnique","isUnique","isUnique","isUnique"]\n[[["deer","door","cake","card"]],["dear"],["cart"],["cane"],["make"]]'
#
# An abbreviation of a word follows the form <first letter><number><last
# letter>. Below are some examples of word abbreviations:
#
#
# a) it                      --> it    (no abbreviation)
#
# ⁠    1
# ⁠    ↓
# b) d|o|g                   --> d1g
#
# ⁠             1    1  1
# ⁠    1---5----0----5--8
# ⁠    ↓   ↓    ↓    ↓  ↓
# c) i|nternationalizatio|n  --> i18n
#
# ⁠             1
# ⁠    1---5----0
# ↓   ↓    ↓
# d) l|ocalizatio|n          --> l10n
#
#
# Assume you have a dictionary and given a word, find whether its abbreviation
# is unique in the dictionary. A word's abbreviation is unique if no other word
# from the dictionary has the same abbreviation.
#
# Example:
#
#
# Given dictionary = [ "deer", "door", "cake", "card" ]
#
# isUnique("dear") -> false
# isUnique("cart") -> true
# isUnique("cane") -> false
# isUnique("make") -> true
#
#
#
class ValidWordAbbr:

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.dic = dict()
        self.words = set()
        for word in dictionary:
            cvt = self._convert(word)
            if cvt in self.dic and word not in self.words:
                self.dic[cvt] = False
            else:
                self.dic[cvt] = True
            self.words.add(word)

    def _convert(self, word):
        if len(word) <= 2:
            return word
        else:
            return word[0]+str(len(word)-2)+word[-1]

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cvt = self._convert(word)
        if cvt not in self.dic:
            return True
        else:
            if word in self.words and self.dic[cvt]:
                return True
            return False


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)
