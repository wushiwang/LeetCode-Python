#
# [158] Read N Characters Given Read4 II - Call multiple times
#
# https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/description/
#
# algorithms
# Hard (24.60%)
# Total Accepted:    42.8K
# Total Submissions: 174K
# Testcase Example:  '""\n[read(0)]'
#
# The API: int read4(char *buf) reads 4 characters at a time from a file.
#
# The return value is the actual number of characters read. For example, it
# returns 3 if there is only 3 characters left in the file.
#
# By using the read4 API, implement the function int read(char *buf, int n)
# that reads n characters from the file.
#
# Note:
# The read function may be called multiple times.
#
# Example 1: 
#
#
# Given buf = "abc"
# read("abc", 1) // returns "a"
# read("abc", 2); // returns "bc"
# read("abc", 1); // returns ""
#
#
# Example 2: 
#
#
# Given buf = "abc"
# read("abc", 4) // returns "abc"
# read("abc", 1); // returns ""
#
#
#
# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):


class Solution(object):
    def __init__(self):
        self.old = []

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        if n <= len(self.old):
            buf[:n] = self.old[:n]
            self.old = self.old[n:]
            return n
        else:
            buf[:len(self.old)] = self.old
            i = len(self.old)
            self.old = []
        tmp = ['', '', '', '']
        t = (n-i) // 4
        for _ in range(t):
            m = read4(tmp)
            buf[i:i+m] = tmp[:m]
            i += m
            if m != 4:
                return i
        if (n-i) % 4 != 0:
            m = read4(tmp)
            if m <= (n-i) % 4:
                buf[i:i+m] = tmp[:m]
                return i+m
            else:
                buf[i:n] = tmp[:(n-i)%4]
                self.old = tmp[(n-i)%4:m]
                i = n
        return i
