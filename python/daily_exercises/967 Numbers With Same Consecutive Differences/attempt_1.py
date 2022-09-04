import copy
from typing import List
class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:

        res = []

        def back_track(current_num, num_list):

            if len(num_list) == n:
               combined = int("".join(str(x) for x in num_list))
               res.append(combined)

            elif len(num_list) > n:
                return

            else:

                for num in range(0, 10, 1):
                    abs_dif = abs(num - current_num)
                    if abs_dif == k:
                        num_list.append(num)
                        back_track(num, num_list)
                        num_list.pop()

        for num in range(1, 10, 1):
            back_track(num, [num])

        return res
