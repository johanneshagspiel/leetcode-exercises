from typing import List
class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:

        boxes.sort(reverse=True)
        box_pointer = 0
        count = 0

        for height in warehouse:

            while box_pointer < len(boxes) and boxes[box_pointer] > height:
                box_pointer += 1

            if box_pointer < len(boxes):
                count += 1
                box_pointer += 1
            else:
                return count

        return count
