from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        columns = len(matrix[0])

        left = 0
        right = (columns * rows) - 1

        while left <= right:
            pivot = ((right + left) // 2)
            pivot_value = matrix[pivot // columns][pivot % columns]

            if pivot_value == target:
                return True
            elif pivot_value < target:
                left = pivot + 1
            else:
                right = pivot - 1

        return False


if __name__ == "__main__":
    solution = Solution()
    matrix = [[1,3]]
    target = 3
    output = solution.searchMatrix(matrix, target)
    print(output)