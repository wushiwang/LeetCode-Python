#
# [500] Keyboard Row
#
# https://leetcode.com/problems/keyboard-row/description/
#
# algorithms
# Easy (60.27%)
# Total Accepted:    67.7K
# Total Submissions: 112.4K
# Testcase Example:  '["Hello","Alaska","Dad","Peace"]'
#
# Given a List of words, return the words that can be typed using letters of
# alphabet on only one row's of American keyboard like the image below.
#
#
#
#
#
#
#
# Example 1:
#
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
#
#
#
# Note:
#
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.
#


class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        kb = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        dic = dict()
        for i in range(len(kb)):
            for c in kb[i]:
                dic[c] = i
        tmp, res = [x.lower() for x in words], []
        for i in range(len(tmp)):
            if len(set([dic[x] for x in tmp[i]])) == 1:
                res.append(words[i])
        return res
