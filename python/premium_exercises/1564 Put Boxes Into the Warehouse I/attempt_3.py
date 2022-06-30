from typing import List
class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:

        boxes.sort()

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
                if inserted[insert_position] == -1:
                    box_count += 1
                else:
                    current_box = inserted[insert_position]
                    current_position = insert_position

                    while current_position - 1 >= 0 and warehouse[current_position - 1] >= current_box:
                        current_position = current_position - 1

                        if inserted[current_position] == -1:
                            inserted[current_position] = current_box
                            box_count += 1
                            break

                inserted[insert_position] = box

        return box_count

