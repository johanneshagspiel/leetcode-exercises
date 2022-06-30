from typing import List
class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:

        boxes.sort(reverse=True)

        left = 0
        right = len(warehouse) - 1

        box_pointer = 0
        counter = 0

        while left <= right:

            if box_pointer == len(boxes):
                return counter

            else:

                current_box = boxes[box_pointer]

                if current_box <= warehouse[left]:
                    left += 1
                    counter += 1

                elif current_box <= warehouse[right]:
                    right -= 1
                    counter += 1

                box_pointer += 1

        return counter