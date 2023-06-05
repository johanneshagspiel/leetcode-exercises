from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        matrix = [[0]*n for _ in range(n)]

        row = 0
        column = 0

        mode = "right"
        num = 1

        change_direction = False

        while True:

            if row < 0 or row >= n or column < 0 or column >= n:
                change_direction = True

            else:
                cur_num = matrix[row][column]

                if cur_num == 0:
                    matrix[row][column] = num
                    num += 1

                    change_direction = False

                    if mode == "right":
                        column += 1
                    elif mode == "down":
                        row += 1
                    elif mode == "left":
                        column -= 1
                    elif mode == "up":
                        row -= 1

                else:
                    change_direction = True

            if change_direction:
                if mode == "right":
                    column -= 1
                    row += 1
                    mode = "down"

                elif mode == "down":
                    row -= 1
                    column -= 1
                    mode = "left"

                elif mode == "left":
                    column += 1
                    row -= 1
                    mode = "up"

                elif mode == "up":
                    row += 1
                    column += 1
                    mode = "right"

            if num == (n*n) + 1:
                return matrix
