from typing import List
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        count_items = 0
        count_boxes = truckSize

        box_index = 0

        while count_boxes >= 0 and box_index < len(boxTypes):
            current_amount_boxes, current_amount_items = boxTypes[box_index]

            amount_boxes_taken = current_amount_boxes if current_amount_boxes <= count_boxes else count_boxes
            count_boxes -= amount_boxes_taken
            count_items += (amount_boxes_taken * current_amount_items)
            box_index += 1

        return count_items

