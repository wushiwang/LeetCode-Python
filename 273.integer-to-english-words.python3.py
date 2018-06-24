#
# [273] Integer to English Words
#
# https://leetcode.com/problems/integer-to-english-words/description/
#
# algorithms
# Hard (22.92%)
# Total Accepted:    62.3K
# Total Submissions: 271.7K
# Testcase Example:  '123'
#
# Convert a non-negative integer to its english words representation. Given
# input is guaranteed to be less than 231 - 1.
#
# Example 1:
#
#
# Input: 123
# Output: "One Hundred Twenty Three"
#
#
# Example 2:
#
#
# Input: 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
#
# Example 3:
#
#
# Input: 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty
# Seven"
#
#
# Example 4:
#
#
# Input: 1234567891
# Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven
# Thousand Eight Hundred Ninety One"
#


class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        self.to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve '\
            'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        self.tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        self.names = ['Billion', 'Million', 'Thousand', 'Hundred']
        if num == 0:
            return "Zero"
        return self.prt(num).strip()

    def prt(self, num):
        if num >= (10**9):
            return self.prt(num//(10**9)).strip() + ' ' +\
                self.names[0] + ' ' + self.prt(num%(10**9)).strip()
        elif num >= (10**6):
            return self.prt(num//(10**6)).strip() + ' ' +\
                self.names[1] + ' ' + self.prt(num%(10**6)).strip()
        elif num >= (10**3):
            return self.prt(num//(10**3)).strip() + ' ' +\
                self.names[2] + ' ' + self.prt(num%(10**3)).strip()
        elif num >= (10**2):
            return self.prt(num//(10**2)).strip() + ' ' +\
                self.names[3] + ' ' + self.prt(num%(10**2)).strip()
        else:
            return self.prt100(num)

    def prt100(self, num):
        if num == 0:
            return ""
        if num < 20:
            return self.to19[num-1]
        else:
            if num%10 == 0:
                return self.tens[(num//10)-2]
            else:
                return self.tens[(num//10)-2]+' '+self.to19[(num%10)-1]
