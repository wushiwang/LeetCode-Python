#
# [93] Restore IP Addresses
#
# https://leetcode.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (28.69%)
# Total Accepted:    105.5K
# Total Submissions: 367.7K
# Testcase Example:  '"25525511135"'
#
# Given a string containing only digits, restore it by returning all possible
# valid IP address combinations.
#
# Example:
#
#
# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]
#


class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.DFS(0, s, res, [], 0)
        return res

    def DFS(self, level, s, res, cur, pos):
        if 4-level > len(s)-pos:
            return
        if level == 4:
            if pos == len(s):
                res.append('.'.join(cur))
            return
        num = 0
        for i in range(1, 4):
            if pos+i < len(s)+1:
                num += int(s[pos+i-1])
                if num <= 255 and ((num == 0 and i == 1) or s[pos] != '0'):
                    self.DFS(level+1, s, res, cur+[s[pos:pos+i]], pos+i)
                num *= 10
