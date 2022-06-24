import heapq
from typing import List
class Solution:
    def isPossible(self, target: List[int]) -> bool:

        self.possible = False
        n = len(target)

        def back_tracking(current_list, current_sum, combined_sum):

            if is_same(current_list, target):
                self.possible = True
                return

            elif current_sum > combined_sum:
                return

            else:

                if current_sum in target:
                    insert_position = target.index(current_sum)
                    current_list[insert_position] = current_sum
                    current_sum = sum(current_list)
                    back_tracking(current_list, current_sum, combined_sum)

                else:

                    heapq.heapify(current_list)

                    for insert_position in range(n):

                        previous_value = current_list[insert_position]

                        current_list[insert_position] = current_sum
                        current_sum  = sum(current_list)

                        back_tracking(current_list, current_sum, combined_sum)

                        current_list[insert_position] = previous_value
                        current_sum  = sum(current_list)


        def is_same(array_1, array_2):
            n = len(array_1)

            for index in range(n):
                if array_1[index] != array_2[index]:
                    return False
            return True


        start_array = [1 for _ in range(n)]
        start_sum = sum(start_array)
        combined_sum = sum(target)

        back_tracking(start_array, start_sum, combined_sum)
        return self.possible
