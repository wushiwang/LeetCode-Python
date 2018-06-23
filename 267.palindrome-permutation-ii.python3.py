#
# [267] Palindrome Permutation II
#
# https://leetcode.com/problems/palindrome-permutation-ii/description/
#
# algorithms
# Medium (32.22%)
# Total Accepted:    18.7K
# Total Submissions: 58K
# Testcase Example:  '"aabb"'
#
# Given a string s, return all the palindromic permutations (without
# duplicates) of it. Return an empty list if no palindromic permutation could
# be form.
#
# Example 1:
#
#
# Input: "aabb"
# Output: ["abba", "baab"]
#
# Example 2:
#
#
# Input: "abc"
# Output: []
#
import collections


class Solution:
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        cnt = collections.Counter(s)
        if len(list(filter(lambda x: x&1 == 1, [v for k, v in cnt.items()]))) > 1:
            return []
        if len(s) & 1 == 1:
            single = list(filter(lambda x: x[1]&1 == 1, list(cnt.items())))[0][0]
        alp = []
        for k, v in cnt.items():
            alp += [k]*(v >> 1)
        res, visited = [], [False for x in range(len(alp))]
        self.generate(alp, res, [], visited)
        if 'single' in vars():
            res = [x+single+x[::-1] for x in res]
        else:
            res = [x+x[::-1] for x in res]
        return res

    def generate(self, alp, res, cur, visited):
        if len(cur) == len(alp):
            res.append(''.join(cur))
            return
        i = 0
        while i < len(alp):
            if not visited[i]:
                visited[i] = True
                self.generate(alp, res, cur+[alp[i]], visited)
                visited[i] = False
                while i+1 < len(alp) and alp[i] == alp[i+1]:
                    i += 1
            i += 1
