from typing import List
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:

        slots1.sort(key = lambda x: x[0])
        slots2.sort(key = lambda x: x[0])

        slot_1_pointer = 0
        slot_2_pointer = 0

        len_slot_1 = len(slots1)
        len_slot_2 = len(slots2)

        result = []

        while slot_1_pointer < len_slot_1 and slot_2_pointer < len_slot_2:
            start_1, end_1 = slots1[slot_1_pointer]
            start_2, end_2 = slots2[slot_2_pointer]

            max_start = max(start_1, start_2)
            min_end = min(end_1, end_2)

            if min_end >= max_start:
                time_slot = min_end - max_start
                if time_slot >= duration:
                    result.append(max_start)
                    result.append((max_start + duration))
                    return result
                else:
                    if end_2 == min_end:
                        slot_2_pointer += 1
                    else:
                        slot_1_pointer += 1

            else:
                if end_2 == min_end:
                    slot_2_pointer += 1
                else:
                    slot_1_pointer += 1

        return result
