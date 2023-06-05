from typing import List


class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:

        boxes.sort(reverse=True)

        len_warehouse = len(warehouse)
        warehouse_pointer = 0

        box_pointer = 0
        len_boxes = len(boxes)

        count = 0

        while warehouse_pointer < len_warehouse:

            current_height = warehouse[warehouse_pointer]

            while box_pointer < len_boxes:
                if boxes[box_pointer] <= current_height:
                    count += 1
                    break
                else:
                    box_pointer += 1

            if box_pointer == len_boxes:
                return count
            else:
                box_pointer += 1

            warehouse_pointer += 1

        return count





