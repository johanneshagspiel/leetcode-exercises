from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_area = 0
        len_height = len(height)

        for index_1, left_wall in enumerate(height):
            for index_2 in range(index_1 + 1, len_height, 1):
                right_wall = height[index_2]
                distance = index_2 - index_1
                height_area = min(left_wall, right_wall)
                area = distance * height_area
                if area > max_area:
                    max_area = area

        return max_area

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxArea([1,8,6,2,5,4,8,3,7]))