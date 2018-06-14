#
# [165] Compare Version Numbers
#
# https://leetcode.com/problems/compare-version-numbers/description/
#
# algorithms
# Medium (21.03%)
# Total Accepted:    102.7K
# Total Submissions: 488.1K
# Testcase Example:  '"0.1"\n"1.1"'
#
# Compare two version numbers version1 and version2.
# If version1 > version2 return 1; if version1 < version2 return -1;otherwise
# return 0.
#
# You may assume that the version strings are non-empty and contain only digits
# and the . character.
# The . character does not represent a decimal point and is used to separate
# number sequences.
# For instance, 2.5 is not "two and a half" or "half way to version three", it
# is the fifth second-level revision of the second first-level revision.
#
# Example 1:
#
#
# Input: version1 = "0.1", version2 = "1.1"
# Output: -1
#
# Example 2:
#
#
# Input: version1 = "1.0.1", version2 = "1"
# Output: 1
#
# Example 3:
#
#
# Input: version1 = "7.5.2.4", version2 = "7.5.3"
# Output: -1
#


class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = list(map(lambda x: int(x), version1.split('.')))
        v2 = list(map(lambda x: int(x), version2.split('.')))
        while len(v1) > 1 and v1[-1] == 0:
            v1.pop()
        while len(v2) > 1 and v2[-1] == 0:
            v2.pop()
        if v1 == v2:
            return 0
        for i in range(min(len(v1), len(v2))):
            if v1[i] < v2[i]:
                return -1
            elif v1[i] > v2[i]:
                return 1
        if len(v1) > len(v2):
            return 1
        elif len(v1) < len(v2):
            return -1
        return 0
