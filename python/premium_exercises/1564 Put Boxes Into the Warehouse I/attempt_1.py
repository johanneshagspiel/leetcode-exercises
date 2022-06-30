from typing import List
class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:

        boxes.sort(reverse=True)

        inserted = [-1 for _ in range(len(warehouse))]
        box_count = 0

        for box in boxes:
            insert_position = -1

            for position, height in enumerate(warehouse):
                if box <= height and inserted[position] < box:
                    insert_position += 1
                else:
                    break

            if insert_position != -1:
                inserted[insert_position] = box
                box_count += 1

        return box_count

