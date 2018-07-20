#
# [527] Word Abbreviation
#
# https://leetcode.com/problems/word-abbreviation/description/
#
# algorithms
# Hard (44.46%)
# Total Accepted:    6K
# Total Submissions: 13.6K
# Testcase Example:  '["like","god","internal","me","internet","interval","intension","face","intrusion"]'
#
# Given an array of n distinct non-empty strings, you need to generate minimal
# possible abbreviations for every word following rules below.
#
#
# Begin with the first character and then the number of characters abbreviated,
# which followed by the last character.
# If there are any conflict, that is more than one words share the same
# abbreviation, a longer prefix is used instead of only the first character
# until making the map from word to abbreviation become unique. In other words,
# a final abbreviation cannot map to more than one original words.
# ⁠If the abbreviation doesn't make the word shorter, then keep it as
# original.
#
#
# Example:
#
# Input: ["like", "god", "internal", "me", "internet", "interval", "intension",
# "face", "intrusion"]
# Output:
# ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
#
#
#
#
# Note:
#
# ⁠Both n and the length of each word will not exceed 400.
# ⁠The length of each word is greater than 1.
# ⁠The words consist of lowercase English letters only.
# ⁠The return answers should be in the same order as the original array.
#


class Solution:
    def wordsAbbreviation(self, dic):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        ab = self.helper(dic, 1)
        res = []
        for word in dic:
            res.append(ab[word])
        return res

    def getAbbrev(self, word):
        if len(word) <= 2:
            return word
        else:
            ab = word[0]+str(len(word)-2)+word[-1]
            if len(ab) < len(word):
                return ab
            else:
                return word

    def helper(self, lst, p):
        cnt = dict()
        for word in lst:
            cur = word[:p-1] + self.getAbbrev(word[p-1:])
            if cur not in cnt:
                cnt[cur] = []
            cnt[cur].append(word)
        ab = dict()
        for k in cnt:
            if len(cnt[k]) == 1:
                ab[cnt[k][0]] = k
            else:
                for r, v in self.helper(cnt[k], p+1).items():
                    ab[r] = v
        return ab
