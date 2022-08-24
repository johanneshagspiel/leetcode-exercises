import operator


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        pairs.sort(key = operator.itemgetter(1))

        prev_end = -float("inf")
        length = 0

        for start, end in pairs:
            if prev_end < start:
                prev_end = end
                length += 1

        return length

