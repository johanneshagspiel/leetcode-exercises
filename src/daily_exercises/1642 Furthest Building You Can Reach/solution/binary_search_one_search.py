from typing import List
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        n = len(heights) - 1
        climbs = []
        for start_index in range(n):
            current_height = heights[start_index]
            next_height = heights[start_index + 1]
            height_difference = next_height - current_height
            if height_difference > 0:
                climbs.append((height_difference, start_index + 1))

        climbs.sort(key=lambda x: x[0])

        left_pointer = 0
        right_pointer = n

        while left_pointer <= right_pointer:
            pivot = left_pointer + ((right_pointer - left_pointer) // 2)

            if self.is_reachable(pivot, climbs, bricks, ladders):
                left_pointer = pivot + 1
            else:
                right_pointer = pivot - 1

        return right_pointer

    def is_reachable(self, pivot, climbs, bricks, ladders):

        remaining_bricks = bricks
        remaining_ladders = ladders

        for climb, index in climbs:
            if index <= pivot:
                if remaining_bricks >= climb:
                    remaining_bricks -= climb
                elif remaining_ladders > 0:
                    remaining_ladders -= 1
                else:
                    return False

        return True