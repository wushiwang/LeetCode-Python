#
# [68] Text Justification
#
# https://leetcode.com/problems/text-justification/description/
#
# algorithms
# Hard (20.23%)
# Total Accepted:    71.9K
# Total Submissions: 354.7K
# Testcase Example:  '["This", "is", "an", "example", "of", "text", "justification."]\n16'
#
# Given an array of words and a width maxWidth, format the text such that each
# line has exactly maxWidth characters and is fully (left and right)
# justified.
#
# You should pack your words in a greedy approach; that is, pack as many words
# as you can in each line. Pad extra spaces ' ' when necessary so that each
# line has exactly maxWidth characters.
#
# Extra spaces between words should be distributed as evenly as possible. If
# the number of spaces on a line do not divide evenly between words, the empty
# slots on the left will be assigned more spaces than the slots on the right.
#
# For the last line of text, it should be left justified and no extra space is
# inserted between words.
#
# Note:
#
#
# A word is defined as a character sequence consisting of non-space characters
# only.
# Each word's length is guaranteed to be greater than 0 and not exceed
# maxWidth.
# The input array words contains at least one word.
#
#
# Example 1:
#
#
# Input:
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# Output:
# [
# "This    is    an",
# "example  of text",
# "justification.  "
# ]
#
#
# Example 2:
#
#
# Input:
# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16
# Output:
# [
# "What   must   be",
# "acknowledgment  ",
# "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall
# be",
# because the last line must be left-justified instead of fully-justified.
# ⁠            Note that the second line is also left-justified becase it
# contains only one word.
#
#
# Example 3:
#
#
# Input:
# words =
# ["Science","is","what","we","understand","well","enough","to","explain",
# "to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20
# Output:
# [
# "Science  is  what we",
# ⁠ "understand      well",
# "enough to explain to",
# "a  computer.  Art is",
# "everything  else  we",
# "do                  "
# ]
#


class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        # [)
        L, R, cur_len = 0, 1, len(words[0])
        res = list()
        while R < len(words):
            if cur_len + len(words[R]) + 1 <= maxWidth:
                cur_len, R = cur_len + len(words[R]) + 1, R + 1
            else:
                gap, tmp, t, n = maxWidth - cur_len, words[L], R - L - 1, 1
                L += 1
                if L == R:
                    tmp = tmp + ' '*gap
                else:
                    while L != R:
                        if n <= gap % t:
                            tmp = tmp + ' '*(gap//t+2) + words[L]
                        else:
                            tmp = tmp + ' '*(gap//t+1) + words[L]
                        L, n = L + 1, n + 1
                res.append(tmp)
                L, R, cur_len = R, R+1, len(words[R])
        if L != R:
            tmp, L = words[L], L + 1
            while L != R:
                tmp = tmp + ' ' + words[L]
                L = L + 1
            tmp = tmp + ' '*(maxWidth - len(tmp))
            res.append(tmp)
        return res
