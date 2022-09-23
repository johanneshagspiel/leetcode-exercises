from typing import List


class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:

        res = []

        remove_start = toBeRemoved[0]
        remove_end = toBeRemoved[1]

        for start, end in intervals:

            max_start = max(remove_start, start)
            min_end = min(remove_end, end)

            if max_start > min_end:
                res.append((start, end))

            elif max_start == remove_start and min_end == remove_end:
                if start != max_start:
                    res.append((start, max_start))
                if end != min_end:
                    res.append((min_end, end))

            elif start < max_start and end > max_start:
                res.append((start, max_start))

            elif start == max_start and end > min_end:
                res.append((min_end, end))


        return res
