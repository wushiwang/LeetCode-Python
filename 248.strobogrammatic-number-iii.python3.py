#
# [248] Strobogrammatic Number III
#
# https://leetcode.com/problems/strobogrammatic-number-iii/description/
#
# algorithms
# Hard (32.94%)
# Total Accepted:    12K
# Total Submissions: 36.4K
# Testcase Example:  '"50"\n"100"'
#
# A strobogrammatic number is a number that looks the same when rotated 180
# degrees (looked at upside down).
#
# Write a function to count the total strobogrammatic numbers that exist in the
# range of low <= num <= high.
#
# Example:
#
#
# Input: low = "50", high = "100"
# Output: 3
# Explanation: 69, 88, and 96 are three strobogrammatic numbers.
#
# Note:
# Because the range might be a large number, the low and high numbers are
# represented as string.
#


class Solution:
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        self.dic = {-1: -1,
                    0: 0,
                    1: 1,
                    2: 1,
                    3: 1,
                    4: 1,
                    5: 1,
                    6: 2,
                    7: 2,
                    8: 3,
                    9: 4}
        self.dic1 = {0: 1,
                     1: 2,
                     2: 2,
                     3: 2,
                     4: 2,
                     5: 2,
                     6: 2,
                     7: 2,
                     8: 3,
                     9: 3}
        self.dic2 = {0: 0,
                     1: 1,
                     6: 9,
                     8: 8,
                     9: 6}

        high = int(high)
        low = int(low)
        if (high < low):
            return 0
        low -= 1
        high = [int(x) for x in str(high)]
        if low == -1:
            return self.numUnderValue(high, high[0], high[-1], True) +\
                self.numOfDigit(len(high)-1)

        low = [int(x) for x in str(low)]
        return self.numUnderValue(high, high[0], high[-1], True) -\
            self.numUnderValue(low, low[0], low[-1], True) +\
            self.numOfDigit(len(high)-1) - \
            self.numOfDigit(len(low)-1)

    def numUnderValue(self, num, L, R, start):
        if len(num) == 0:
            return 0
        if len(num) == 1:
            if start:
                return self.dic1[num[0]]
            else:
                return self.dic1[num[0]]
        if L in self.dic2:
            if R >= self.dic2[L]:
                if len(num) == 2:
                    ext = 1
                else:
                    ext = 0
                if start:
                    return ((self.dic[L-1]+ext)*self.nod(len(num)-2)) +\
                        (self.numUnderValue(num[1:-1], num[1], num[-2], False))
                else:
                    return ((self.dic[L-1]+1+ext)*self.nod(len(num)-2)) +\
                        (self.numUnderValue(num[1:-1], num[1], num[-2], False))
            else:
                j = len(num)-2
                while j != 0 and num[j] == 0:
                    j -= 1
                if j == 0:
                    tmp = 0
                else:
                    num[j] -= 1
                    j += 1
                    while j != len(num)-1:
                        num[j] = 9
                        j += 1
                    tmp = self.numUnderValue(num[1:-1], num[1], num[-2], False)
                if start:
                    return ((self.dic[L-1])*self.nod(len(num)-2)) +\
                        tmp
                else:
                    return ((self.dic[L-1]+1)*self.nod(len(num)-2)) +\
                        tmp
        else:
            if start:
                return (self.dic[L-1])*self.nod(len(num)-2)
            else:
                return (self.dic[L-1]+1)*self.nod(len(num)-2)

    def numOfDigit(self, n):
        if n <= 0:
            return 0
        if n == 1:
            return 3
        if n & 1 == 1:
            return 4*(5**((n-2)//2))*3 + self.numOfDigit(n-1)
        else:
            return 4*(5**((n-2)//2)) + self.numOfDigit(n-1)

    def nod(self, n):
        if n <= 0:
            return 1
        if n & 1:
            return (5**(n//2))*3
        else:
            return (5**(n//2))
