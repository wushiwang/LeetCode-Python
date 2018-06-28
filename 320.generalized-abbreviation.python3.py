#
# [320] Generalized Abbreviation
#
# https://leetcode.com/problems/generalized-abbreviation/description/
#
# algorithms
# Medium (46.57%)
# Total Accepted:    30.6K
# Total Submissions: 65.6K
# Testcase Example:  '"word"'
#
# Write a function to generate the generalized abbreviations of a word. 
#
# Note: The order of the output does not matter.
#
# Example:
#
#
# Input: "word"
# Output:
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1",
# "w1r1", "1o2", "2r1", "3d", "w3", "4"]
#


class Solution:
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        res = []
        self.DFS(word, 0, "", res)
        return res

    def DFS(self, word, num, cur, res):
        if word == '':
            if num != 0:
                cur += str(num)
            res.append(cur)
            return
        self.DFS(word[1:], num+1, cur, res)
        if num != 0:
            self.DFS(word[1:], 0, cur+str(num)+word[0], res)
        else:
            self.DFS(word[1:], 0, cur+word[0], res)
