
class Trie:

    def __init__(self):
        self.children = {}
        self.end = 0
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        n = len(grid)

        root = Trie()

        for row in range(n):
            node = root
            for column in range(n):
                current_num = grid[row][column]

                if current_num not in node.children:
                    node.children[current_num] = Trie()
                node = node.children[current_num]
            node.end += 1

        count = 0
        for column in range(n):
            node = root
            found = True

            for row in range(n):
                current_num = grid[row][column]

                if current_num not in node.children:
                    found = False
                    break
                else:
                    node = node.children[current_num]

            if found:
                count += node.end

        return count
