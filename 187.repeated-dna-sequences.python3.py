#
# [187] Repeated DNA Sequences
#
# https://leetcode.com/problems/repeated-dna-sequences/description/
#
# algorithms
# Medium (33.36%)
# Total Accepted:    97.5K
# Total Submissions: 292.1K
# Testcase Example:  '"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"'
#
# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
# for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to
# identify repeated sequences within the DNA.
#
# Write a function to find all the 10-letter-long sequences (substrings) that
# occur more than once in a DNA molecule.
#
# Example:
#
#
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
#
# Output: ["AAAAACCCCC", "CCCCCAAAAA"]
#


class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []
        use = {'A': 0, 'C': 1, 'G': 2, 'T':3}
        mask = (1 << 20) - 1
        dic, res = dict(), []
        cur, L, R = 0, 0, 0
        while R != 9:
            cur <<= 2
            cur |= use[s[R]]
            R += 1
        while R < len(s):
            cur <<= 2
            cur |= use[s[R]]
            cur &= mask
            if cur not in dic:
                dic[cur] = 1
            elif dic[cur] == 1:
                dic[cur] += 1
                res.append(s[L:R+1])
            L, R = L+1, R+1
        return res
