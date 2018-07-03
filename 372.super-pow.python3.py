#
# [372] Super Pow
#
# https://leetcode.com/problems/super-pow/description/
#
# algorithms
# Medium (34.79%)
# Total Accepted:    21.8K
# Total Submissions: 62.7K
# Testcase Example:  '2\n[3]'
#
#
# Your task is to calculate ab mod 1337 where a is a positive integer and b is
# an extremely large positive integer given in the form of an array.
#
#
# Example1:
#
# a = 2
# b = [3]
#
# Result: 8
#
#
#
# Example2:
#
# a = 2
# b = [1,0]
#
# Result: 1024
#
#
#
# Credits:Special thanks to @Stomach_ache for adding this problem and creating
# all test cases.



class Solution:
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        b = int(''.join(map(lambda x: str(x), b)))
        return self.pow(a % 1337, b)

    def pow(self, x, y):
        res, cur = 1, x
        while y != 0:
            if y & 1 == 1:
                res *= cur
                res %= 1337
            cur *= cur
            cur %= 1337
            y >>= 1
        return res
