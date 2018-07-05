#
# [393] UTF-8 Validation
#
# https://leetcode.com/problems/utf-8-validation/description/
#
# algorithms
# Medium (34.85%)
# Total Accepted:    23.7K
# Total Submissions: 67.9K
# Testcase Example:  '[197,130,1]'
#
# A character in UTF8 can be from 1 to 4 bytes long, subjected to the following
# rules:
#
# For 1-byte character, the first bit is a 0, followed by its unicode code.
# For n-bytes character, the first n-bits are all one's, the n+1 bit is 0,
# followed by n-1 bytes with most significant 2 bits being 10.
#
# This is how the UTF-8 encoding would work:
#
# ⁠  Char. number range  |        UTF-8 octet sequence
# ⁠     (hexadecimal)    |              (binary)
# ⁠  --------------------+---------------------------------------------
# ⁠  0000 0000-0000 007F | 0xxxxxxx
# ⁠  0000 0080-0000 07FF | 110xxxxx 10xxxxxx
# ⁠  0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
# ⁠  0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
#
#
# Given an array of integers representing the data, return whether it is a
# valid utf-8 encoding.
#
#
# Note:
# The input is an array of integers. Only the least significant 8 bits of each
# integer is used to store the data. This means each integer represents only 1
# byte of data.
#
#
#
# Example 1:
#
# data = [197, 130, 1], which represents the octet sequence: 11000101 10000010
# 00000001.
#
# Return true.
# It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte
# character.
#
#
#
#
# Example 2:
#
# data = [235, 140, 4], which represented the octet sequence: 11101011 10001100
# 00000100.
#
# Return false.
# The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes
# character.
# The next byte is a continuation byte which starts with 10 and that's correct.
# But the second continuation byte does not start with 10, so it is invalid.
#


class Solution:
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        mask1 = [0x00000000, 0x000000C0, 0x000000E0, 0x000000F0]
        mask2 = [0x00000080, 0x00000020, 0x00000010, 0x00000008]
        mask3 = 0x00000080
        mask4 = 0x00000040
        i = 0
        while i < len(data):
            j = 0
            while j < 4:
                if data[i] & mask1[j] == mask1[j] and\
                        data[i] & mask2[j] == 0:
                    break
                j += 1
            if j == 4:
                return False
            for k in range(i+1, i+j+1):
                if k < len(data):
                    if not (data[k] & mask3 == mask3 and data[k] & mask4 == 0):
                        return False
                else:
                    return False
            i = i+j+1
        return True
