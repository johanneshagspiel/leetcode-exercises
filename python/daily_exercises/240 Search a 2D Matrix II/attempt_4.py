from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix:
            return False

        n = len(matrix)
        m = len(matrix[0])

        def binary_search(start, vertical):

            left = start

            if vertical:
                right = n - 1
            else:
                right = m - 1

            while left <= right:
                pivot = left + ((right - left) // 2)

                if vertical:
                    pivot_num = matrix[pivot][start]
                else:
                    pivot_num = matrix[start][pivot]

                if pivot_num == target:
                    return True
                elif pivot_num < target:
                    left = pivot + 1
                else:
                    right = pivot - 1

            return False

        for i in range(min(n, m)):
            vertical_res = binary_search(i, True)
            horizontal_res = binary_search(i, False)

            if vertical_res or horizontal_res:
                return True

        return False

