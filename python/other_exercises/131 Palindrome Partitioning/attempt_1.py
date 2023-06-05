from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []

        n = len(s)

        def rec(index, result):

            if index == n:
                res.append(result[::])

            else:

                for position in range(index, n):
                    option = s[index:(position + 1)]

                    if option == option[::-1]:
                        result.append(option)
                        rec(position + 1, result)
                        result.pop()

        rec(0, [])
        return res
