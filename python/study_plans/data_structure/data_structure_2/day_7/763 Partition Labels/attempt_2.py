from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        index = {c:i for i, c in enumerate(s)}

        j = 0
        anchor = 0
        res = []

        for i, c in enumerate(s):

            j = max(j, index[c])

            if i == j:
                dis = i - anchor + 1
                res.append(dis)
                anchor = i + 1

        return res

