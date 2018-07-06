#
# [401] Binary Watch
#
# https://leetcode.com/problems/binary-watch/description/
#
# algorithms
# Easy (44.78%)
# Total Accepted:    50.1K
# Total Submissions: 111.8K
# Testcase Example:  '0'
#
# A binary watch has 4 LEDs on the top which represent the hours (0-11), and
# the 6 LEDs on the bottom represent the minutes (0-59).
# Each LED represents a zero or one, with the least significant bit on the
# right.
#
# For example, the above binary watch reads "3:25".
#
# Given a non-negative integer n which represents the number of LEDs that are
# currently on, return all possible times the watch could represent.
#
# Example:
# Input: n = 1Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04",
# "0:08", "0:16", "0:32"]
#
#
# Note:
#
# The order of output does not matter.
# The hour must not contain a leading zero, for example "01:00" is not valid,
# it should be "1:00".
# The minute must be consist of two digits and may contain a leading zero, for
# example "10:2" is not valid, it should be "10:02".
#


class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        for i in range(0, num+1):
            if i <= 4 and (num-i) <= 6:
                h, m = [], []
                self.DFS_H(i, h, 0, 0, 0)
                self.DFS_M(num-i, m, 0, 0, 0)
                for hh in h:
                    for mm in m:
                        res.append("{x}:{y:02d}".format(x=hh, y=mm))
        return res

    def DFS_H(self, n, res, cur, ones, level):
        if ones > n:
            return
        if level == 4:
            if ones == n:
                if cur <= 11:
                    res.append(cur)
            return
        self.DFS_H(n, res, cur, ones, level+1)
        self.DFS_H(n, res, cur | (1 << level), ones+1, level+1)

    def DFS_M(self, n, res, cur, ones, level):
        if ones > n:
            return
        if level == 6:
            if ones == n:
                if cur <= 59:
                    res.append(cur)
            return
        self.DFS_M(n, res, cur, ones, level+1)
        self.DFS_M(n, res, cur | (1 << level), ones+1, level+1)
