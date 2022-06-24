from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result_list = []
        n = len(candidates)

        def back_tracking(remaining, current_list, start_index):

            if remaining == 0:
                result_list.append(current_list[::])
                return

            elif remaining < 0:
                return

            else:

                for index in range(start_index, n):

                    remaining -= candidates[index]
                    current_list.append(candidates[index])

                    back_tracking(remaining, current_list, index)

                    remaining += candidates[index]
                    current_list.pop()

        back_tracking(target, [], 0)
        return result_list

