#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (39.12%)
# Total Accepted:    204.7K
# Total Submissions: 522.6K
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings, group anagrams together.
#
# Example:
#
#
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
# ⁠ ["ate","eat","tea"],
# ⁠ ["nat","tan"],
# ⁠ ["bat"]
# ]
#
# Note:
#
#
# All inputs will be in lowercase.
# The order of your output does not matter.
#


class myStr(str):
    @property
    def normalized(self):
        try:
            return self._normalized
        except AttributeError:
            self._normalized = ''.join(sorted(list(self)))
        return self._normalized

    def __hash__(self):
        return hash(self.normalized)

    def __eq__(self, other):
        return self.normalized == other.normalized


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for s in strs:
            ns = myStr(s)
            if ns in dic:
                dic[ns].append(s)
            else:
                dic[ns] = [s]
        return list(dic.values())
