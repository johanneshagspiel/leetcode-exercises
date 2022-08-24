import operator


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        pairs.sort(key = operator.itemgetter(1))

        res = 0
        prev_end = -float("inf")

        for start, end in pairs:
            if prev_end < start:
                prev_end = end
                res += 1

        return res
