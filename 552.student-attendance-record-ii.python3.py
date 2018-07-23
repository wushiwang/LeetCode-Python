#
# [552] Student Attendance Record II
#
# https://leetcode.com/problems/student-attendance-record-ii/description/
#
# algorithms
# Hard (31.85%)
# Total Accepted:    8.7K
# Total Submissions: 27.2K
# Testcase Example:  '1'
#
# Given a positive integer n, return the number of all possible attendance
# records with length n, which will be regarded as rewardable. The answer may
# be very large, return it after mod 109 + 7.
#
# A student attendance record is a string that only contains the following
# three characters:
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
# A record is regarded as rewardable if it doesn't contain more than one 'A'
# (absent) or more than two continuous 'L' (late).
#
# Example 1:
#
# Input: n = 2
# Output: 8
# Explanation:
# There are 8 records with length 2 will be regarded as rewardable:
# "PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# Only "AA" won't be regarded as rewardable owing to more than one absent
# times.
#
#
#
# Note:
# The value of n won't exceed 100,000.
#


class Solution:
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = int(1e9+7)
        A, AL, AM, AP, L, M, P = 1, 0, 0, 0, 1, 0, 1
        i = 1
        while i < n:
            NA = (L + M + P) % MOD
            NAL = (A + AP) % MOD
            NAM = AL % MOD
            NAP = (A + AL + AM + AP) % MOD
            NL = P % MOD
            NM = L % MOD
            NP = (L + M + P) % MOD
            A, AL, AM, AP, L, M, P = NA, NAL, NAM, NAP, NL, NM, NP
            i += 1
        return sum([A, AL, AM, AP, L, M, P]) % MOD
