from typing import List
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        priority_list = [((-1)*x[1], x[0]) for x in boxTypes]
        heapq.heapify(priority_list)

        count = 0

        while truckSize > 0 and len(priority_list) > 0:
            current_item_amount, current_box_amount = heapq.heappop(priority_list)

            boxes_selected = current_box_amount if current_box_amount <= truckSize else truckSize
            truckSize -= boxes_selected
            count += (boxes_selected * (current_item_amount * (-1)))

        return count
