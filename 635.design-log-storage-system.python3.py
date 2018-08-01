#
# [635] Design Log Storage System
#
# https://leetcode.com/problems/design-log-storage-system/description/
#
# algorithms
# Medium (49.59%)
# Total Accepted:    5.2K
# Total Submissions: 10.4K
# Testcase Example:  '["LogSystem","put","put","put","retrieve","retrieve"]\n[[],[1,"2017:01:01:23:59:59"],[2,"2017:01:01:22:59:59"],[3,"2016:01:01:00:00:00"],["2016:01:01:01:01:01","2017:01:01:23:00:00","Year"],["2016:01:01:01:01:01","2017:01:01:23:00:00","Hour"]]'
#
# You are given several logs that each log contains a unique id and timestamp.
# Timestamp is a string that has the following format:
# Year:Month:Day:Hour:Minute:Second, for example, 2017:01:01:23:59:59. All
# domains are zero-padded decimal numbers.
#
# Design a log storage system to implement the following functions:
#
# void Put(int id, string timestamp): Given a log's unique id and timestamp,
# store the log in your storage system.
#
# int[] Retrieve(String start, String end, String granularity): Return the id
# of logs whose timestamps are within the range from start to end. Start and
# end all have the same format as timestamp. However, granularity means the
# time level for consideration. For example, start = "2017:01:01:23:59:59", end
# = "2017:01:02:23:59:59", granularity = "Day", it means that we need to find
# the logs within the range from Jan. 1st 2017 to Jan. 2nd 2017.
#
# Example 1:
#
# put(1, "2017:01:01:23:59:59");
# put(2, "2017:01:01:22:59:59");
# put(3, "2016:01:01:00:00:00");
# retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year"); // return
# [1,2,3], because you need to return all logs within 2016 and 2017.
# retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Hour"); // return
# [1,2], because you need to return all logs start from 2016:01:01:01 to
# 2017:01:01:23, where log 3 is left outside the range.
#
# Note:
#
# There will be at most 300 operations of Put or Retrieve.
# Year ranges from [2000,2017]. Hour ranges from [00,23].
# Output for Retrieve has no order required.
#
import bisect


class LogSystem:

    def __init__(self):
        self.storage = []
        self.dic = dict()

    def put(self, id, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        bisect.insort(self.storage, timestamp)
        self.dic[timestamp] = id

    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        if len(self.storage) == 0:
            return []
        l = {'Year': 4,
             'Month': 7,
             'Day': 10,
             'Hour': 13,
             'Minute': 16,
             'Second': 19}
        ll = {'Year': ':00:00:00:00:00',
              'Month': ':00:00:00:00',
              'Day': ':00:00:00',
              'Hour': ':00:00',
              'Minute': ':00',
              'Second': ''}
        lll = {'Year': ':99:99:99:99:99',
              'Month': ':99:99:99:99',
              'Day': ':99:99:99',
              'Hour': ':99:99',
              'Minute': ':99',
              'Second': ''}

        s = s[:l[gra]] + ll[gra]
        e = e[:l[gra]] + lll[gra]
        L = bisect.bisect_left(self.storage, s)
        if L == len(self.storage):
            return []
        if self.storage[L] < s:
            L += 1
        R = bisect.bisect_right(self.storage, e)
        res = []
        for i in range(L, R):
            res.append(self.dic[self.storage[i]])
        return res


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)
