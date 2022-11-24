class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        max_rows = len(board)
        max_columns = len(board[0])

        def bfs(start_row, start_column, word):

            stack = []
            stack.append((start_row, start_column, 1))
            moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            seen_set = set()

            while stack:

                current_row, current_column, index = stack.pop()
                # board[current_row][current_column] = "#"
                seen_set.add((current_row, current_column))

                if index == len(word):
                    return True
                else:
                    for row_move, column_move in moves:
                        new_row = current_row + row_move
                        new_column = current_column + column_move

                        if new_row >= 0 and new_row < max_rows and new_column >= 0 and new_column < max_columns:
                            if (new_row, new_column) not in seen_set:
                                target_char = word[index]
                                other_char = board[new_row][new_column]
    
                                if target_char == other_char:
                                    stack.append((new_row, new_column, index + 1))
            return False

        for row in range(max_rows):
            for column in range(max_columns):
                char = board[row][column]

                if char == word[0]:
                    result = bfs(row, column, word)
                    if result:
                        return True

        return False
