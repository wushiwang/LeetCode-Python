#
# [249] Group Shifted Strings
#
# https://leetcode.com/problems/group-shifted-strings/description/
#
# algorithms
# Medium (44.93%)
# Total Accepted:    35.9K
# Total Submissions: 79.8K
# Testcase Example:  '["abc","bcd","acef","xyz","az","ba","a","z"]'
#
# Given a string, we can "shift" each of its letter to its successive letter,
# for example: "abc" -> "bcd". We can keep "shifting" which forms the
# sequence:
#
#
# "abc" -> "bcd" -> ... -> "xyz"
#
# Given a list of strings which contains only lowercase alphabets, group all
# strings that belong to the same shifting sequence.
#
# Example:
#
#
# Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
# Output:
# [
# ⁠ ["abc","bcd","xyz"],
# ⁠ ["az","ba"],
# ⁠ ["acef"],
# ⁠ ["a","z"]
# ]
#


class Solution:
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        dic = dict()
        for w in strings:
            cur = self.shiftToAxx(w)
            if cur not in dic:
                dic[cur] = [w]
            else:
                dic[cur].append(w)
        return [v for k, v in dic.items()]

    def shiftToAxx(self, w):
        if len(w) == 0:
            return w
        if w[0] == 'a':
            return w
        else:
            dis = ord(w[0]) - ord('a')
            nw = ""
            for c in w:
                nc = ord(c) - dis
                if nc < ord('a'):
                    nc += 26
                nw += chr(nc)
        return nw
