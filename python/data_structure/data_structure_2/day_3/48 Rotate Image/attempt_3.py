from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        left = 0
        right = len(matrix[0]) - 1

        while left < right:
            matrix[left], matrix[right] = matrix[right], matrix[left]
            left += 1
            right -= 1


        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
