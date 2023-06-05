from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        matrix = [[0]*n for _ in range(n)]

        num = 1
        fix = 0

        start = 0
        end = n
        inc = 1

        mode = "right"


        while True:

            for position in range(start, end, inc):
                if mode == "right" or mode == "left":
                    matrix[fix][position] = num
                elif mode == "down" or mode == "up":
                    matrix[position][fix] = num

                num += 1

            if mode == "right":
                mode = "down"
                fix = position
                start = 0
                end = n
                inc = 1

            elif mode == "down":
                mode = "left"
                fix = position
                start = n
                end = -1
                inc = -1

            elif mode == "left":
                mode = "up"
                fix = position
                start = n
                end = -1
                inc = -1

            elif mode == "up":
                mode = "right"
                fix = position
                start = 0
                end = n
                inc = 1

