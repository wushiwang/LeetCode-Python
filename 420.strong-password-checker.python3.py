#
# [420] Strong Password Checker
#
# https://leetcode.com/problems/strong-password-checker/description/
#
# algorithms
# Hard (19.45%)
# Total Accepted:    4.8K
# Total Submissions: 24.9K
# Testcase Example:  '""'
#
# A password is considered strong if below conditions are all met:
#
#
# ⁠It has at least 6 characters and at most 20 characters.
# ⁠It must contain at least one lowercase letter, at least one uppercase
# letter, and at least one digit.
# ⁠It must NOT contain three repeating characters in a row ("...aaa..." is
# weak, but "...aa...a..." is strong, assuming other conditions are met).
#
#
# Write a function strongPasswordChecker(s), that takes a string s as input,
# and return the MINIMUM change required to make s a strong password. If s is
# already strong, return 0.
#
# Insertion, deletion or replace of any one character are all considered as one
# change.
#
import heapq


class Solution:
    def strongPasswordChecker(self, s):
        """
        :type s: str
        :rtype: int
        """
        a, A, d = 1, 1, 1
        for c in s:
            if c.islower():
                a = 0
            elif c.isupper():
                A = 0
            elif c.isdigit():
                d = 0
        missing = a + A + d
        rep, i = [], 0
        while i < len(s):
            l = 1
            while i+1 < len(s) and s[i+1] == s[i]:
                l += 1
                i += 1
            if l >= 3:
                rep.append((l%3, l))
            i += 1
        if len(s) < 6:
            return (6 - len(s)) + max(0, missing - (6 - len(s)))
        else:
            delete, total = max(len(s) - 20, 0), len(s)
            heapq.heapify(rep)
            while len(rep) != 0 and total > 20:
                m, v = heapq.heappop(rep)
                delta = min(m+1, total-20)
                total -= delta
                heapq.heappush(rep, (2, v-delta))
            change = sum(v//3 for m, v in rep)
            return delete + max(change, missing)
