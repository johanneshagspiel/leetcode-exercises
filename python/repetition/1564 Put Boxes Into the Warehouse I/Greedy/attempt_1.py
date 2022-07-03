from typing import List
class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:

        boxes.sort(reverse=True)
        count = 0
        box_position = 0
        n = len(boxes)

        for warehouse_height in warehouse:

            while (box_position < n) and (warehouse_height < boxes[box_position]):
                box_position += 1

            if box_position == n:
                return count

            else:
                box_position += 1
                count += 1

        return count