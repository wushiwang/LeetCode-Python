#
# [423] Reconstruct Original Digits from English
#
# https://leetcode.com/problems/reconstruct-original-digits-from-english/description/
#
# algorithms
# Medium (44.82%)
# Total Accepted:    15.4K
# Total Submissions: 34.3K
# Testcase Example:  '"owoztneoer"'
#
# Given a non-empty string containing an out-of-order English representation of
# digits 0-9, output the digits in ascending order.
#
# Note:
#
# Input contains only lowercase English letters.
# Input is guaranteed to be valid and can be transformed to its original
# digits. That means invalid inputs such as "abc" or "zerone" are not
# permitted.
# Input length is less than 50,000.
#
#
#
# Example 1:
#
# Input: "owoztneoer"
#
# Output: "012"
#
#
#
# Example 2:
#
# Input: "fviefuro"
#
# Output: "45"
#
# zero one two three four five six seven eight nine
# z -> zero
# x -> six
# u -> four
# g -> eight
# w -> two
#
# one three five seven nine
# t -> eight, three, two -> three
# f -> four, five -> five
# v -> five, seven -> seven
# i -> six, eight, nine, five -> nine
# o -> zero, four, two, one -> one


class Solution:
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        num = [0 for x in range(10)]
        for c in s:
            if c == 'z':
                num[0] += 1
            if c == 'x':
                num[6] += 1
            if c == 'u':
                num[4] += 1
            if c == 'g':
                num[8] += 1
            if c == 'w':
                num[2] += 1
            if c == 't':
                num[3] += 1
            if c == 'f':
                num[5] += 1
            if c == 'v':
                num[7] += 1
            if c == 'i':
                num[9] += 1
            if c == 'o':
                num[1] += 1
        num[3] = num[3] - num[2] - num[8]
        num[5] = num[5] - num[4]
        num[7] = num[7] - num[5]
        num[9] = num[9] - num[5] - num[6] - num[8]
        num[1] = num[1] - num[0] - num[4] - num[2]
        res = ''
        for i in range(10):
            if num[i] != 0:
                res += str(i)*num[i]
        return res
