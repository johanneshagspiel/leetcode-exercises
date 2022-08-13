from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        result_list = []

        def create_combs(start_num, current_list):

            if len(current_list) == k:
                result_list.append(current_list[::])

            else:
                for number in range(start_num, n+1):
                    current_list.append(start_num)
                    create_combs(number+1, current_list)
                    current_list.pop()

        create_combs(1, [])
        return result_list
