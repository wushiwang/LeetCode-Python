#
# [394] Decode String
#
# https://leetcode.com/problems/decode-string/description/
#
# algorithms
# Medium (42.09%)
# Total Accepted:    58.5K
# Total Submissions: 138.8K
# Testcase Example:  '"3[a]2[bc]"'
#
#
# Given an encoded string, return it's decoded string.
#
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the
# square brackets is being repeated exactly k times. Note that k is guaranteed
# to be a positive integer.
#
#
# You may assume that the input string is always valid; No extra white spaces,
# square brackets are well-formed, etc.
#
# Furthermore, you may assume that the original data does not contain any
# digits and that digits are only for those repeat numbers, k. For example,
# there won't be input like 3a or 2[4].
#
#
# Examples:
#
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
#


class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        def isNum(c):
            return ord(c) >= ord('0') and ord(c) <= ord('9')
        stack, i = [], 0
        while i < len(s):
            if isNum(s[i]):
                j = i+1
                while j < len(s) and isNum(s[j]):
                    j += 1
                stack.append(int(s[i:j]))
                i = j+1
            elif s[i] == ']':
                v = stack.pop()
                n = stack.pop()
                if len(stack) == 0 or type(stack[-1]) is int:
                    stack.append(v*n)
                else:
                    stack[-1] += v*n
                i += 1
            else:
                if len(stack) == 0 or type(stack[-1]) is int:
                    stack.append(s[i])
                else:
                    stack[-1] += s[i]
                i += 1
        return stack[-1] if len(stack) != 0 else ""
