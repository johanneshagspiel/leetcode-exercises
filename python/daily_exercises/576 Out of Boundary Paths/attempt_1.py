class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        def out_of_bounds(row, column):
            if row < 0 or row >= m or column < 0 or column >= n:
                return True
            else:
                return False


        def back_track(moves_left, row, column, mem_dic):
            if moves_left >= 0 and out_of_bounds(row, column):
                return 1

            elif moves_left <= 0:
                return 0

            elif (row, column, moves_left) in mem_dic:
                return mem_dic[(row, column, moves_left)]

            else:

                moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                total = 0

                for row_move, column_move in moves:
                    new_row = row + row_move
                    new_column = column + column_move
                    total += back_track(moves_left - 1, new_row, new_column, mem_dic)

                mem_dic[(row, column, moves_left)] = total

                return total

        res = back_track(maxMove, startRow, startColumn, {})

        return res % (pow(10, 9) + 7)
