from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:

        max_area = 0
        left_pointer = 0
        right_pointer = len(height) - 1

        while left_pointer < right_pointer and left_pointer < len(height) and right_pointer:
            distance = right_pointer - left_pointer
            height_area = min(height[left_pointer], height[right_pointer])
            temp_area = distance * height_area
            if temp_area > max_area:
                max_area = temp_area

            left_pointer += 1
            distance = right_pointer - left_pointer
            height_area = min(height[left_pointer], height[right_pointer])
            temp_area_left = distance * height_area
            left_pointer -= 1

            right_pointer -= 1
            distance = right_pointer - left_pointer
            height_area = min(height[left_pointer], height[right_pointer])
            temp_area_right = distance * height_area
            right_pointer += 1

            if temp_area_left > temp_area_right:
                left_pointer += 1
            else:
                right_pointer += 1



        return max_area

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
    max_area = 0
