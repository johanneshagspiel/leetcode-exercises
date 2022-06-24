import collections
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        result_list = []
        counter = collections.Counter(candidates)
        counter_table = [(c, counter[c]) for c in counter]
        n = len(counter_table)

        def back_track(remaining, current_list, current_index, counter_table):

            if remaining == 0:
                result_list.append(current_list[::])
                return
            elif remaining < 0:
                return
            else:
                for index in range(current_index, len(counter_table)):
                    number, frequency = counter_table[index]

                    if frequency < 0:
                        continue

                    current_list.append(number)
                    counter_table[index] = number, frequency - 1

                    back_track(remaining - number, current_list, index, counter_table)

                    current_list.pop()
                    counter_table[index] = number, frequency

        back_track(target, [], 0, counter_table)
        return result_list


