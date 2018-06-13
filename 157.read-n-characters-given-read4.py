#
# [157] Read N Characters Given Read4
#
# https://leetcode.com/problems/read-n-characters-given-read4/description/
#
# algorithms
# Easy (28.63%)
# Total Accepted:    50.5K
# Total Submissions: 176.4K
# Testcase Example:  '""\n0'
#
# The API: int read4(char *buf) reads 4 characters at a time from a file.
#
# The return value is the actual number of characters read. For example, it
# returns 3 if there is only 3 characters left in the file.
#
# By using the read4 API, implement the function int read(char *buf, int n)
# that reads n characters from the file.
#
# Example 1:
#
#
# Input: buf = "abc", n = 4
# Output: "abc"
# Explanation: The actual number of characters read is 3, which is "abc".
#
#
# Example 2:
#
#
# Input: buf = "abcde", n = 5
# Output: "abcde"
#
#
# Note:
# The read function will only be called once for each test case.
#
#
# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):


class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        if n == 0:
            return 0
        i, tmp = 0, [0, 0, 0, 0]
        while i <= n:
            m = read4(tmp)
            if i + m <= n:
                buf[i:i+m] = tmp[:m]
            else:
                buf[i:i+n-i] = tmp[:n-i]
                return n
            i += m
            if m != 4:
                return i
        return n
