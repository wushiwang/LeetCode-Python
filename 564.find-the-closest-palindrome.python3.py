#
# [564] Find the Closest Palindrome
#
# https://leetcode.com/problems/find-the-closest-palindrome/description/
#
# algorithms
# Hard (16.86%)
# Total Accepted:    6.5K
# Total Submissions: 38.6K
# Testcase Example:  '"1"'
#
# Given an integer n, find the closest integer (not including itself), which is
# a palindrome.
#
# The 'closest' is defined as absolute difference minimized between two
# integers.
#
# Example 1:
#
# Input: "123"
# Output: "121"
#
#
#
# Note:
#
# The input n is a positive integer represented by string, whose length will
# not exceed 18.
# If there is a tie, return the smaller one as answer.
#
import math


class Solution:
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        m = len(n)
        pot = [pow(10, m)+1, pow(10, m-1)-1]
        if m & 1 == 1:
            pot.append(int(n[:(m//2)+1]+n[:m//2][::-1]))
            if n[m//2] == '0':
                pot.append(int(n[:(m//2)]+'9'+n[:m//2][::-1]))
            else:
                pot.append(int(n[:(m//2)]+str(int(n[m//2])-1)+n[:m//2][::-1]))
            pot.append(int(n[:(m//2)]+str(int(n[m//2])+1)[0]+n[:m//2][::-1]))
        else:
            pot.append(int(n[:m//2]+n[:m//2][::-1]))
            if n[m//2-1] == '0':
                pot.append(int(n[:(m//2)-1]+'99'+n[:(m//2)-1][::-1]))
            else:
                pot.append(int(n[:(m//2)-1]+str(int(n[(m//2)-1])-1)*2+n[:(m//2)-1][::-1]))
            pot.append(int(n[:(m//2)-1]+str(int(n[(m//2)-1])+1)[0]*2+n[:(m//2)-1][::-1]))
        n, dis, res = int(n), math.inf, None
        for p in pot:
            cur = int(abs(p-n))
            if cur != 0:
                if cur < dis:
                    dis, res = cur, p
                elif cur == dis and p < res:
                    dis, res = cur, p
        return str(res)
