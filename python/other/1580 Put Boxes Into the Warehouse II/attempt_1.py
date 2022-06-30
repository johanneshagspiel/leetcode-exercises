from typing import List
class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:

        boxes.sort(reverse=True)
        left = 0
        right = len(warehouse) - 1
        count = 0
        box_pointer = 0

        while left < right:

            if box_pointer == len(boxes):
                return count

            else:
                current_box = boxes[box_pointer]

                if current_box <= warehouse[right]:
                    count += 1
                    right -= 1

                elif current_box <= warehouse[left]:
                    count += 1
                    left += 1

                box_pointer += 1

        return count

