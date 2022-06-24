from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        rows = len(matrix)
        columns = len(matrix[0])

        new_matrix = [[0]*rows for column in range(columns)]

        for row in range(rows):
            for column in range(columns):
                new_matrix[column][row] = matrix[row][column]

        return new_matrix

if __name__ == '__main__':
    solution = Solution()
    matrix = [[1,2,3],[4,5,6]]
    output = solution.transpose(matrix)
    print(output)