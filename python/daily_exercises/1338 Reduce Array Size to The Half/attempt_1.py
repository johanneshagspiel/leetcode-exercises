import collections
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        N = len(arr)// 2
        counter = collections.Counter(arr)

        priority_list = []

        for number, count in counter.items():
            priority_list.append((count, number))

        priority_list.sort(key=lambda x: x[0], reverse=True)

        res = 0

        for count, number in priority_list:
            N -= count
            res += 1

            if N <= 0:
                return res

        return res
