from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)

        for row in range(m):
            row_list = matrix[row]
            first_entry = row_list[0]
            last_entry = row_list[-1]

            if first_entry == target or last_entry == target:
                return True

            if first_entry < target < last_entry:
                smaller_list = row_list[1:-1]
                return self.binary_search(smaller_list, target)

        return False


    def binary_search(self, list, target):
        left = 0
        right = len(list) - 1

        while left <= right:
            pivot = left + ((right - left) // 2)
            pivot_value = list[pivot]

            if target == pivot_value:
                return True
            elif target < pivot_value:
                right = pivot - 1
            else:
                left = pivot + 1

        return False


if __name__ == "__main__":
    solution = Solution()
    matrix = [[1,3,5]]
    target = 3
    output = solution.searchMatrix(matrix, target)
    print(output)