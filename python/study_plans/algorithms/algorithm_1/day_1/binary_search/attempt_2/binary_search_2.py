from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.search_with_start_index(nums=nums, target=target, start_index=0)

    def search_with_start_index(self, nums: List[int], target: int, start_index: int) -> int:

        if len(nums) == 1:
            return start_index if nums[0] == target else -1

        half_way_index = int(len(nums) / 2)
        half_way_value = nums[half_way_index]

        if half_way_value == target:
            return start_index + half_way_index

        elif half_way_value < target:
            return self.search_with_start_index(nums=nums[half_way_index:], target=target, start_index=start_index + half_way_index)

        elif half_way_value > target:
            return self.search_with_start_index(nums=nums[:half_way_index], target=target, start_index=start_index)

if __name__ == '__main__':
    solution = Solution()

    input_1 = [-1,0,3,5,9,12]
    target_1 = 9
    output_1 = solution.search(input_1, target_1)
    expected_1 = 4

    print(1)
    print(output_1)
    print(output_1 == expected_1)
    print(" ")


    input_2 = [-1,0,3,5,9,12]
    target_2 = 2
    output_2 = solution.search(input_2, target_2)
    expected_2 = -1

    print(2)
    print(output_2)
    print(output_2 == expected_2)
    print(" ")

    input_3 = [-1,0,3,5,9,12]
    target_3 = 12
    output_3 = solution.search(input_3, target_3)
    expected_3 = 5

    print(3)
    print(output_3)
    print(output_3 == expected_3)
    print(" ")
