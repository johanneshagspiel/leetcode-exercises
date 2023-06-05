from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        result_list = []

        def rec(start_number, current_list):

            if len(current_list) == k:
                result_list.append(current_list[::])
            else:
                for number in range(start_number, n+1):
                    current_list.append(number)
                    rec(number+1, current_list)
                    current_list.pop()

        rec(1, [])
        return result_list