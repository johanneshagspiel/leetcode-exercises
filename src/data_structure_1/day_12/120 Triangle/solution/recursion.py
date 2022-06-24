class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n_rows = len(triangle)

        def mover_helper(current_row, current_index, move_dic):
            move_dic_key = (str(current_row) + "-" + str(current_index))

            if current_row == n_rows:
                return 0
            elif current_row == (n_rows - 1):
                return triangle[current_row][current_index]
            elif move_dic_key in move_dic:
                return move_dic[move_dic_key]
            else:
                min_moves = triangle[current_row][current_index] + min(mover_helper(current_row + 1, current_index, move_dic), mover_helper(current_row + 1, current_index + 1, move_dic))
                move_dic[move_dic_key] = min_moves
                return min_moves

        return mover_helper(0, 0, {})