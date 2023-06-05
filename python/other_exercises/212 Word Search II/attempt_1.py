class Trie:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        result = set()

        def back_track(row, column, parent):

            letter = board[row][column]
            trie = parent.children[letter]

            board[row][column] = "#"

            moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            if trie.word:
                result.add(trie.word)
                trie.word = None

            for row_move, column_move in moves:
                new_row = row + row_move
                new_column = column + column_move

                if new_row >= 0 and new_row < max_rows and new_column >= 0 and new_column < max_columns:

                    next_char = board[new_row][new_column]

                    if next_char in trie.children:
                        back_track(new_row, new_column, trie)

            board[row][column] = letter

            if not trie:
                parent.children.pop(letter)

        root = Trie()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = Trie()
                node = node.children[char]
            node.word = word

        max_rows = len(board)
        max_columns = len(board[0])

        for row in range(max_rows):
            for column in range(max_columns):
                char = board[row][column]

                if char in root.children:
                    back_track(row, column, root)

        return result
