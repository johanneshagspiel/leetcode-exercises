from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        n = len(numbers)
        result_list = []

        for first_pointer in range(n):
            first_value = numbers[first_pointer]
            missing_value = target - first_value

            left_pointer = first_pointer + 1
            right_pointer = n - 1

            while left_pointer <= right_pointer:
                pivot = left_pointer + ((right_pointer - left_pointer) // 2)
                pivot_value = numbers[pivot]

                if pivot_value == missing_value:
                    return [first_pointer + 1, pivot + 1]
                    break
                elif pivot_value < missing_value:
                    left_pointer = pivot + 1
                else:
                    right_pointer = pivot - 1

if __name__ == "__main__":
    solution = Solution()
    solution.twoSum([2,7,11,15], target=9)