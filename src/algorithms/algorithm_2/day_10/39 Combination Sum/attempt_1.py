from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result_list = []
        n = len(candidates)

        def back_track(current_list, current_sum, start_index):

            if current_sum == target:
                result_list.append(current_list[::])
                return

            if start_index == n:
                return 

            else:
                counter = 0
                while (current_sum + (counter * candidates[start_index])) <= target:

                    current_sum += (counter * candidates[start_index])

                    for _ in range(counter):
                        current_list.append(candidates[start_index])

                    back_track(current_list, current_sum, start_index + 1)

                    current_sum -= (counter * candidates[start_index])

                    for _ in range(counter):
                        current_list.pop()

                    counter += 1

        back_track([], 0, 0)
        return result_list

