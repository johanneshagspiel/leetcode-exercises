import collections
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:

        if len(changed) % 2 != 0:
            return []

        counter = collections.Counter(changed)

        changed.sort(reverse=False)
        #changed = self.counting_sort(changed)

        doubles_encountered = len(changed) / 2
        res = []

        for num in changed:
            if counter[num] > 0:
                half = num / 2
                if half in counter and counter[half] > 0:
                    counter[half] -= 1
                    counter[num] -= 1

                    if counter[half] < 0 or counter[num] < 0:
                        counter[half] += 1
                        counter[num] += 1
                    else:
                        doubles_encountered -= 1
                        res.append(int(half))

        if doubles_encountered == 0:
            return res
        else:
            return []

    def counting_sort(self, input):

        min_num = min(input)
        max_num = max(input)

        count_array = [0 for _ in range(min_num, max_num + 1)]

        for num in input:
            count_array[num - min_num] += 1

        res = []

        for index, count in enumerate(count_array):
            if count > 0:
                temp_count = count
                while temp_count > 0:
                    res.append(index + min_num)
                    temp_count -= 1

        return res


