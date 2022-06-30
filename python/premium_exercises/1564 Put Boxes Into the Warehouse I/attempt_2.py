from typing import List
class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:

        possible_insertions = [[(-1, -1)] for _ in range(len(warehouse))]

        for index, box in enumerate(boxes):

            for position, height in enumerate(warehouse):
                if box <= height:
                    possible_insertions[position].append((index, box))
                else:
                    break


        taken_set = set()
        count = 0

        for position_list in possible_insertions:
            if len(position_list) > 1:
                position_list.sort(key=lambda x:x[1], reverse=True)

                for index, height in position_list:
                    key = str(index) + "_" + str(height)

                    if key not in taken_set and key != "-1_-1":
                        count += 1
                        taken_set.add(key)
                        break

        return count
