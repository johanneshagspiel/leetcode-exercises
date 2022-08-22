import collections


class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        counter = collections.Counter(arr)
        largest_count = max(counter.values())

        bucket = [0] * (largest_count + 1)

        for count in counter.values():
            bucket[count] += 1

        res = 0
        target = len(arr) // 2

        for index in range(largest_count, -1, -1):
            while bucket[index] > 0:
                res += 1
                target -= index
                bucket[index] -= 1

                if target <= 0:
                    return res

        return res
