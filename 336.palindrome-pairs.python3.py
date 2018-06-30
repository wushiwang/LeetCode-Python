#
# [336] Palindrome Pairs
#
# https://leetcode.com/problems/palindrome-pairs/description/
#
# algorithms
# Hard (27.38%)
# Total Accepted:    41K
# Total Submissions: 149.7K
# Testcase Example:  '["abcd","dcba","lls","s","sssll"]'
#
#
# ⁠   Given a list of unique words, find all pairs of distinct indices (i, j)
# in the given list, so that the concatenation of the two words, i.e. words[i]
# + words[j] is a palindrome.
#
#
#
# ⁠   Example 1:
# ⁠   Given words = ["bat", "tab", "cat"]
# ⁠   Return [[0, 1], [1, 0]]
# ⁠   The palindromes are ["battab", "tabbat"]
#
#
# ⁠   Example 2:
# ⁠   Given words = ["abcd", "dcba", "lls", "s", "sssll"]
# ⁠   Return [[0, 1], [1, 0], [3, 2], [2, 4]]
# ⁠   The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
#
#
# Credits:Special thanks to @dietpepsi for adding this problem and creating all
# test cases.
#


class Solution:
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        dic = dict()
        for i in range(len(words)):
            if words[i] not in dic:
                dic[words[i]] = [i]
            else:
                dic[words[i]].append(i)
        res = []
        for i in range(len(words)):
            pos = len(words[i])
            while pos >= 0:
                fixed = words[i][pos:]
                left = words[i][:pos]
                if fixed == fixed[::-1]:
                    if left[::-1] in dic:
                        for j in dic[left[::-1]]:
                            if i != j:
                                res.append([i, j])
                pos -= 1
            pos = 1
            while pos <= len(words[i]):
                fixed = words[i][:pos]
                left = words[i][pos:]
                if fixed == fixed[::-1]:
                    if left[::-1] in dic:
                        for j in dic[left[::-1]]:
                            if i != j:
                                res.append([j, i])
                pos += 1
        return res
