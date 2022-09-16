import collections
from typing import List

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:

        if len(changed) % 2 != 0:
            return []

        max_value = max(changed)

        doubles_needed = len(changed) // 2
        counter = collections.Counter(changed)

        res = []

        for num in range(max_value + 1):

            if num in counter:
                while counter[num] > 0:
                    counter[num] -= 1

                    double = num * 2

                    if double in counter and counter[double] > 0:
                        counter[double] -= 1
                        res.append(num)
                        doubles_needed -= 1
                    else:
                        return []

        if doubles_needed == 0:
            return res
        else:
            return []

