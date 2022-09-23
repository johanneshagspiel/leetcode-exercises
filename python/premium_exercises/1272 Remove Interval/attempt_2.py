class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:

        remove_start = toBeRemoved[0]
        remove_end = toBeRemoved[1]

        res = []

        for start, end in intervals:

            min_end = min(remove_start, end)
            max_start = max(remove_end, start)

            if start < min_end:
                res.append((start, min_end))

            if end > max_start:
                res.append((max_start, end))

        return res
