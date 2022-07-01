from typing import List
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x:x[1], reverse=True)
        box_index = 0
        count = 0

        while truckSize > 0 and box_index < len(boxTypes):
            box_amount, item_amount = boxTypes[box_index]
            boxes_selected = box_amount if box_amount <= truckSize else truckSize
            truckSize -= boxes_selected
            count += (boxes_selected * item_amount)
            box_index += 1

        return count