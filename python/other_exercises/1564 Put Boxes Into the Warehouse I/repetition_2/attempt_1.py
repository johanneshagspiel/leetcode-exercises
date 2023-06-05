from typing import List
class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:

        boxes.sort(reverse=True)
        box_pointer = 0
        N = len(boxes)
        counter = 0

        for position in warehouse:
            while box_pointer < N and boxes[box_pointer] > position:
                box_pointer += 1

            if box_pointer == N:
                return counter

            else:
                counter += 1
                box_pointer += 1

        return counter
