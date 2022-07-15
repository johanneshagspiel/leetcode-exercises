from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        result_list = []

        def back_track(start_index, current_list):

            if len(current_list) == k:
                result_list.append(current_list[::])

            elif start_index > n:
                return

            else:

                for number in range(start_index, n+1):
                    current_list.append(number)
                    back_track(number+1, current_list)
                    current_list.pop()

        back_track(1, [])
        return result_list
