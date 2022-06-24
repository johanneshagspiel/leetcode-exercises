from typing import List
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights) - 1
        left_pointer = 0
        right_pointer = n

        while left_pointer < right_pointer:
            pivot = left_pointer + ((right_pointer - left_pointer + 1) // 2)

            if self.is_reachable(pivot, heights, bricks, ladders):
                left_pointer = pivot
            else:
                right_pointer = pivot - 1

        return left_pointer


    def is_reachable(self, pivot, heights, bricks, ladders):

        climbs=[]

        for start_point in range(pivot):
            current_point= heights[start_point]
            next_point = heights[start_point + 1]

            if next_point > current_point:
                height_difference = next_point - current_point
                climbs.append(height_difference)

        climbs.sort()

        bricks_remaining = bricks
        ladders_remaining = ladders

        for climb in climbs:

            if climb <= bricks_remaining:
                bricks_remaining -= climb
            elif ladders_remaining > 0:
                ladders_remaining -= 1
            else:
                return False

        return True

if __name__ == "__main__":
    solution = Solution()
    solution.furthestBuilding([4,2,7,6,9,14,12],5,1)