#
# [444] Sequence Reconstruction
#
# https://leetcode.com/problems/sequence-reconstruction/description/
#
# algorithms
# Medium (19.55%)
# Total Accepted:    11.2K
# Total Submissions: 57K
# Testcase Example:  '[1,2,3]\n[[1,2],[1,3]]'
#
# Check whether the original sequence org can be uniquely reconstructed from
# the sequences in seqs. The org sequence is a permutation of the integers from
# 1 to n, with 1 ≤ n ≤ 104. Reconstruction means building a shortest common
# supersequence of the sequences in seqs (i.e., a shortest sequence so that all
# sequences in seqs are subsequences of it). Determine whether there is only
# one sequence that can be reconstructed from seqs and it is the org sequence.
#
# Example 1:
#
# Input:
# org: [1,2,3], seqs: [[1,2],[1,3]]
#
# Output:
# false
#
# Explanation:
# [1,2,3] is not the only one sequence that can be reconstructed, because
# [1,3,2] is also a valid sequence that can be reconstructed.
#
#
#
# Example 2:
#
# Input:
# org: [1,2,3], seqs: [[1,2]]
#
# Output:
# false
#
# Explanation:
# The reconstructed sequence can only be [1,2].
#
#
#
# Example 3:
#
# Input:
# org: [1,2,3], seqs: [[1,2],[1,3],[2,3]]
#
# Output:
# true
#
# Explanation:
# The sequences [1,2], [1,3], and [2,3] can uniquely reconstruct the original
# sequence [1,2,3].
#
#
#
# Example 4:
#
# Input:
# org: [4,1,5,2,6,3], seqs: [[5,2,6,3],[4,1,5,2]]
#
# Output:
# true
#
#
#
#
# UPDATE (2017/1/8):
# The seqs parameter had been changed to a list of list of strings (instead of
# a 2d array of strings). Please reload the code definition to get the latest
# changes.
#


class Solution:
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        graph = dict()
        ind = dict()
        for seq in seqs:
            if len(seq) == 1:
                if seq[0] not in graph:
                    graph[seq[0]] = set()
                    ind[seq[0]] = 0
            for i in range(1, len(seq)):
                if seq[i-1] not in graph:
                    graph[seq[i-1]] = set()
                    ind[seq[i-1]] = 0
                if seq[i] not in graph:
                    graph[seq[i]] = set()
                    ind[seq[i]] = 0
                if seq[i] not in graph[seq[i-1]]:
                    graph[seq[i-1]].add(seq[i])
                    ind[seq[i]] += 1
        if len(graph) != len(set(org)):
            return False
        que, pos = [], 0
        for k in ind:
            if ind[k] == 0:
                que.append(k)
        while len(que) != 0:
            if len(que) != 1:
                return False
            cur = que.pop()
            if pos >= len(org) or cur != org[pos]:
                return False
            for nxt in graph[cur]:
                ind[nxt] -= 1
                if ind[nxt] == 0:
                    que.append(nxt)
            pos += 1
        if pos != len(org):
            return False
        return True
