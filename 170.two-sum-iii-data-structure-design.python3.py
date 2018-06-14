#
# [170] Two Sum III - Data structure design
#
# https://leetcode.com/problems/two-sum-iii-data-structure-design/description/
#
# algorithms
# Easy (26.78%)
# Total Accepted:    38.9K
# Total Submissions: 145.2K
# Testcase Example:  '["TwoSum","add","add","add","find","find"]\n[[],[1],[3],[5],[4],[7]]'
#
# Design and implement a TwoSum class. It should support the following
# operations: add and find.
#
# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the
# value.
#
# Example 1:
#
#
# add(1); add(3); add(5);
# find(4) -> true
# find(7) -> false
#
#
# Example 2:
#
#
# add(3); add(1); add(2);
# find(3) -> true
# find(6) -> false
#
#
class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = dict()
        self.rec = set()

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        if number not in self.dic:
            self.dic[number] = 1
        else:
            self.dic[number] += 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        if value in self.rec:
            return True
        else:
            for k in self.dic:
                if value-k in self.dic:
                    if (value-k == k and self.dic[k] > 1) or value-k != k :
                        self.rec.add(value)
                        return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
