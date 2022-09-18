from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        solution = []

        n = len(s)

        def back_tracking(index, current_list):

            if index == n:
                solution.append(current_list[::])

            else:

                for position in range(index, n):
                    candidate = s[index:(position+1)]

                    if candidate == candidate[::-1]:
                        current_list.append(candidate)
                        back_tracking(position + 1, current_list)
                        current_list.pop()

        back_tracking(0, [])
        return solution

