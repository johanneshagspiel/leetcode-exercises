import collections


class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:

        n = len(changed)

        if n % 2 == 1:
            return []

        counter = collections.Counter(changed)
        max_value = max(changed)

        res = []

        for num in range(max_value):
            if num in counter:
                if counter[num] > 0:
                    counter[num] -= 1

                    double = num * 2

                    if double in counter and counter[double] > 0:
                        counter[double] -= 1
                        res.append(num)
                    else:
                        return []

        return res

