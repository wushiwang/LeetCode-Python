#
# [379] Design Phone Directory
#
# https://leetcode.com/problems/design-phone-directory/description/
#
# algorithms
# Medium (36.92%)
# Total Accepted:    15.9K
# Total Submissions: 43.1K
# Testcase Example:  '["PhoneDirectory","get","get","check","get","check","release","check"]\n[[3],[],[],[2],[],[2],[2],[2]]'
#
# Design a Phone Directory which supports the following operations:
#
#
#
# get: Provide a number which is not assigned to anyone.
# check: Check if a number is available or not.
# release: Recycle or release a number.
#
#
#
# Example:
#
# // Init a phone directory containing a total of 3 numbers: 0, 1, and 2.
# PhoneDirectory directory = new PhoneDirectory(3);
#
# // It can return any available phone number. Here we assume it returns 0.
# directory.get();
#
# // Assume it returns 1.
# directory.get();
#
# // The number 2 is available, so return true.
# directory.check(2);
#
# // It returns 2, the only number that is left.
# directory.get();
#
# // The number 2 is no longer available, so return false.
# directory.check(2);
#
# // Release number 2 back to the pool.
# directory.release(2);
#
# // Number 2 is available again, return true.
# directory.check(2);
#
import heapq


class PhoneDirectory:

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.heap = [(0, 0)]
        self.mx = maxNumbers
        self.dic = set()

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        val, typ = self.heap[0]
        if val == self.mx:
            return -1
        else:
            if typ == 0:
                self.heap = [(val+1, typ)]
            else:
                heapq.heappop(self.heap)
            self.dic.add(val)
            return val

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        if number >= self.mx or number < 0:
            return False
        return not number in self.dic

    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: void
        """
        if number in self.dic:
            heapq.heappush(self.heap, (number, 1))
            self.dic.remove(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
