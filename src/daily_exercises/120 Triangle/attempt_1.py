from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        rows = len(triangle)

        for row in range(rows - 2, -1, -1):
            columns = len(triangle[row])

            for column in range(columns):
                previous_row_element = triangle[row + 1][column]
                previous_row_element_1 = triangle[row + 1][column + 1]

                triangle[row][column] = triangle[row][column] + min(previous_row_element, previous_row_element_1)

        return triangle[0][0]

if __name__ == "__main__":
    solution = Solution()
    solution.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])