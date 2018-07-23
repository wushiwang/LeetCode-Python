#
# [551] Student Attendance Record I
#
# https://leetcode.com/problems/student-attendance-record-i/description/
#
# algorithms
# Easy (44.80%)
# Total Accepted:    36.5K
# Total Submissions: 81.5K
# Testcase Example:  '"PPALLP"'
#
# You are given a string representing an attendance record for a student. The
# record only contains the following three characters:
#
#
#
# 'A' : Absent.
# 'L' : Late.
# ⁠'P' : Present.
#
#
#
#
# A student could be rewarded if his attendance record doesn't contain more
# than one 'A' (absent) or more than two continuous 'L' (late).
#
# You need to return whether the student could be rewarded according to his
# attendance record.
#
# Example 1:
#
# Input: "PPALLP"
# Output: True
#
#
#
# Example 2:
#
# Input: "PPALLL"
# Output: False
#


class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return True
        ab, late, i = 0, False, 0
        while i < len(s):
            if s[i] == 'A':
                ab += 1
            elif s[i] == 'L':
                cnt = 1
                while i+1 < len(s) and s[i+1] == 'L':
                    cnt += 1
                    i += 1
                if cnt > 2:
                    late = True
            i += 1
        return ab <= 1 and (not late)
