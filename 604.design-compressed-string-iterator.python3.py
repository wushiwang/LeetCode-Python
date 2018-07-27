#
# [604] Design Compressed String Iterator
#
# https://leetcode.com/problems/design-compressed-string-iterator/description/
#
# algorithms
# Easy (33.56%)
# Total Accepted:    9.4K
# Total Submissions: 28K
# Testcase Example:  '["StringIterator","next","next","next","next","next","next","hasNext","next","hasNext"]\n[["L1e2t1C1o1d1e1"],[],[],[],[],[],[],[],[],[]]'
#
#
# Design and implement a data structure for a compressed string iterator. It
# should support the following operations: next and hasNext.
#
#
#
# The given compressed string will be in the form of each letter followed by a
# positive integer representing the number of this letter existing in the
# original uncompressed string.
#
#
#
# next() - if the original string still has uncompressed characters, return the
# next letter; Otherwise return a white space.
# hasNext() - Judge whether there is any letter needs to be uncompressed.
#
#
#
# Note:
# Please remember to RESET your class variables declared in StringIterator, as
# static/class variables are persisted across multiple test cases. Please see
# here for more details.
#
#
#
# Example:
#
# StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");
#
# iterator.next(); // return 'L'
# iterator.next(); // return 'e'
# iterator.next(); // return 'e'
# iterator.next(); // return 't'
# iterator.next(); // return 'C'
# iterator.next(); // return 'o'
# iterator.next(); // return 'd'
# iterator.hasNext(); // return true
# iterator.next(); // return 'e'
# iterator.hasNext(); // return false
# iterator.next(); // return ' '
#


class StringIterator:

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.rec = compressedString
        self.char, self.n, self.pos = self._getTocken(compressedString, 0)

    def _getTocken(self, compressedString, pos):
        if pos == len(compressedString):
            return ' ', 0, pos
        char = compressedString[pos]
        pos += 1
        start = pos
        while pos < len(compressedString) and compressedString[pos].isdigit():
            pos += 1
        return char, int(compressedString[start:pos]), pos

    def next(self):
        """
        :rtype: str
        """
        if self.pos == len(self.rec) and self.n == 0:
            return ' '
        res = self.char
        self.n -= 1
        if self.n == 0:
            self.char, self.n, self.pos = self._getTocken(self.rec, self.pos)
        return res


    def hasNext(self):
        """
        :rtype: bool
        """
        if self.pos == len(self.rec):
            return self.n != 0
        else:
            return True


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
