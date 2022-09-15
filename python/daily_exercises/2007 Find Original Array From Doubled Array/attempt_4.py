import collections
from typing import List


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:

        n = len(changed)

        if n % 2 == 1:
            return []

        max_value = max(changed)
        counter = collections.Counter(changed)

        doubles_encountered = len(changed) // 2

        res = []

        for num in range(max_value+1):

            if num in counter:

                while counter[num] > 0:
                    counter[num] -= 1
                    double = 2 * num

                    if double in counter:
                        res.append(num)
                        counter[double] -= 1
                        doubles_encountered -= 1
                    else:
                        return []

        if doubles_encountered == 0:
            return res
        else:
            return []
