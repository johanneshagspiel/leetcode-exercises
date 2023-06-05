class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        rows = len(matrix)
        columns = len(matrix[0])

        if rows == 0:
            return []

        res = [(matrix[0][0])]

        seen = set()
        seen.add((0, 0))

        moves = [(0, 1), (-1, 0), (0, -1), (1, 0)]

        move_position = 0

        tried_moves = 0

        keep_going = True

        current_row = 0
        current_column = 0


        while keep_going:

            potential_row = current_row + moves[move_position][0]
            potential_column = current_column + moves[move_position][1]

            if potential_row >= 0 and potential_row < rows and potential_column >= 0 and potential_column < columns and (potential_row, potential_column) not in seen:
                seen.add((potential_row, potential_column))
                res.append(matrix[potential_row][potential_column])

                current_row = potential_row
                current_column = potential_column

                tried_moves = 0

            else:
                tried_moves += 1

                if tried_moves == 4:
                    keep_going = False

                move_position += 1
                move_position = move_position % 4

        return res



