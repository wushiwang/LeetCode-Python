#
# [681] Next Closest Time
#
# https://leetcode.com/problems/next-closest-time/description/
#
# algorithms
# Medium (41.44%)
# Total Accepted:    20.2K
# Total Submissions: 48.8K
# Testcase Example:  '"19:34"'
#
# Given a time represented in the format "HH:MM", form the next closest time by
# reusing the current digits. There is no limit on how many times a digit can
# be reused.
#
# You may assume the given input string is always valid. For example, "01:34",
# "12:09" are all valid. "1:34", "12:9" are all invalid.
#
# Example 1:
#
# Input: "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39,
# which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours
# and 59 minutes later.
#
#
#
# Example 2:
#
# Input: "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
# It may be assumed that the returned time is next day's time since it is
# smaller than the input time numerically.
#


class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        start = time
        time = set(time[:2]+time[3:])
        res, res_dis = start, 1440
        for i in time:
            for j in time:
                for k in time:
                    for h in time:
                        cur = i+j+':'+k+h
                        if int(cur[:2]) <= 23 and int(cur[3:]) <= 59:
                            dis = self.dis(start, cur)
                            if dis < res_dis:
                                res_dis, res = dis, cur
        return res

    def dis(self, a, b):
        x, y = int(a[:2])*60+int(a[3:]), int(b[:2])*60+int(b[3:])
        if y > x:
            return y-x
        else:
            return y-x+1440
