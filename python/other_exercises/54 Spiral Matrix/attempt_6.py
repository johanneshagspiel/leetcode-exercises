class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        top = 0
        bottom = len(matrix) - 1

        left = 0
        right = len(matrix[0]) - 1

        res = []

        while (left <= right) and (top <= bottom):

            for column in range(left, right + 1, 1):
                res.append(matrix[top][column])
            top += 1

            for row in range(top, bottom + 1, 1):
                res.append(matrix[row][right])
            right -= 1

            for column in range(right, left - 1, -1):
                res.append(matrix[bottom][column])
            bottom -= 1

            for row in range(bottom, top - 1, -1):
                res.append(matrix[row][left])
            left += 1

        return res[:(len(matrix) * len(matrix[0]))]
