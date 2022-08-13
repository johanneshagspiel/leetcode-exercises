from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:

        min_val = float("inf")
        min_ind = -1
        max_val = -float("inf")
        max_ind = -1

        for index, value in enumerate(salary):

            if value < min_val:
                min_val = value
                min_ind = index

            if value > max_val:
                max_val = value
                max_ind = index

        if min_ind < max_ind:
            max_ind = max_ind - 1

        salary.pop(min_ind)
        salary.pop(max_ind)

        avg = sum(salary) / len(salary)

        return avg
