
# [616] Add Bold Tag in String
#
# https://leetcode.com/problems/add-bold-tag-in-string/description/
#
# algorithms
# Medium (38.09%)
# Total Accepted:    13.5K
# Total Submissions: 35.4K
# Testcase Example:  '"abcxyz123"\n["abc","123"]'
#
# Given a string s and a list of strings dict, you need to add a closed pair of
# bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two
# such substrings overlap, you need to wrap them together by only one pair of
# closed bold tag. Also, if two substrings wrapped by bold tags are
# consecutive, you need to combine them.
#
# Example 1:
#
# Input:
# s = "abcxyz123"
# dict = ["abc","123"]
# Output:
# "<b>abc</b>xyz<b>123</b>"
#
#
#
# Example 2:
#
# Input:
# s = "aaabbcc"
# dict = ["aaa","aab","bc"]
# Output:
# "<b>aaabbc</b>c"
#
#
#
# Note:
#
# The given dict won't contain duplicates, and its length won't exceed 100.
# All the strings in input have length in range [1, 1000].
#


class Solution:
    def addBoldTag(self, s, dic):
        """
        :type s: str
        :type dict: List[str]
        :rtype: str
        """
        if len(dic) == 0 or len(s) == 0:
            return s
        intervals = []
        for word in dic:
            pos = 0
            res = s.find(word, pos)
            while res != -1:
                intervals.append((res, res+len(word)-1))
                pos = res + 1
                res = s.find(word, pos)
        if len(intervals) == 0:
            return s
        intervals = sorted(intervals)
        stack = [intervals[0]]
        for i in range(1, len(intervals)):
            cur = intervals[i]
            if cur[0] <= stack[-1][1] + 1:
                old = stack.pop()
                stack.append((old[0], max(old[1], cur[1])))
            else:
                stack.append(cur)
        res, pos = '', 0
        for i in range(len(s)):
            if pos == len(stack):
                res += s[i]
            else:
                if i == stack[pos][0]:
                    res += '<b>'
                res += s[i]
                if i == stack[pos][1]:
                    res += '</b>'
                    pos += 1
        return res
