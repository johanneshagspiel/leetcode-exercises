from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:

        min_index = min(ratings)
        n = len(ratings)
        count = ratings[0] - min_index + 1

        modes_array = []
        current_mode = None
        current_mode_index = -1

        for index in range(1,n):
            if ratings[index] > ratings[index -1]:
                if current_mode == "INC":
                    modes_array[current_mode_index][1] += 1
                else:
                    current_mode_index += 1
                    modes_array.append(("INC", 1))
                    current_mode = "INC"

            elif ratings[index] == ratings[index -1]:
                if current_mode == "EQ":
                    modes_array[current_mode_index][1] += 1
                else:
                    current_mode_index += 1
                    modes_array.append(("EQ", 1))
                    current_mode = "EQ"

            else:
                if current_mode == "DEC":
                    modes_array[current_mode_index][1] += 1
                else:
                    current_mode_index += 1
                    modes_array.append(("DEC", 1))
                    current_mode = "DEC"

        return modes_array
