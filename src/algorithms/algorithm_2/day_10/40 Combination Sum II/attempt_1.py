import collections
import json
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        counter = collections.Counter(candidates)
        result_list = []
        seen = set()

        def back_tracking(remaining, current_list, counter):

            if remaining == 0:

                current_list.sort()
                key = json.dumps(current_list)
                if key not in seen:
                    seen.add(key)
                    result_list.append(current_list[::])
                    return
            elif remaining < 0:
                return
            else:

                for number in counter:
                    if counter[number] > 0:
                        amount = counter[number]

                        for current_amount in range(1, amount + 1):

                            for _ in range(current_amount):
                                current_list.append(number)
                            remaining -= (current_amount * number)
                            counter[number] = 0

                            back_tracking(remaining, current_list, counter)

                            for _ in range(current_amount):
                                current_list.pop()
                            remaining += (current_amount * number)
                            counter[number] = amount

        back_tracking(target, [], counter)
        return result_list

