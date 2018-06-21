#
# [247] Strobogrammatic Number II
#
# https://leetcode.com/problems/strobogrammatic-number-ii/description/
#
# algorithms
# Medium (41.19%)
# Total Accepted:    30.3K
# Total Submissions: 73.6K
# Testcase Example:  '2'
#
# A strobogrammatic number is a number that looks the same when rotated 180
# degrees (looked at upside down).
#
# Find all strobogrammatic numbers that are of length = n.
#
# Example:
#
#
# Input:  n = 2
# Output: ["11","69","88","96"]
#


class Solution:
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        valid = {'1': '1',
                 '6': '9',
                 '8': '8',
                 '9': '6',
                 '0': '0'}
        if n == 1:
            return ['1', '8', '0']
        res = ['1', '6', '8', '9']
        for i in range(1, n//2):
            tmp = []
            for j in valid:
                for r in res:
                    tmp.append(r+j)
            res = tmp
        if n&1 == 1:
            tmp = []
            for j in ['1', '8', '0']:
                for r in res:
                    tmp.append(r+j)
            res = [x+''.join([valid[y] for y in x[:-1][::-1]]) for x in tmp]
        else:
            res = [x+''.join([valid[y] for y in x[::-1]]) for x in res]
        return res
