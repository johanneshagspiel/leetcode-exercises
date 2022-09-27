class DUS:

    def __init__(self):
        self.parent = [i for i in range(26)]
        self.rank = [0 for _ in range(26)]

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)

        if parent_a == parent_b:
            return False
        else:
            rank_p_a = self.rank[parent_a]
            rank_p_b = self.rank[parent_b]

            if rank_p_a > rank_p_b:
                self.parent[parent_b] = parent_a
                self.rank[parent_a] += 1
            elif rank_p_a < rank_p_b:
                self.parent[parent_a] = parent_b
                self.rank[parent_b] += 1
            else:
                self.parent[parent_b] = parent_a
                self.rank[parent_a] += 1

            return True


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        dus = DUS()

        for equation in equations:
            letter_1 = ord(equation[0]) - ord('a')
            sign = equation[1:3]
            letter_2 = ord(equation[3]) - ord('a')

            if sign == "==":
                dus.union(letter_1, letter_2)

        for equation in equations:
            letter_1 = ord(equation[0]) - ord('a')
            sign = equation[1:3]
            letter_2 = ord(equation[3]) - ord('a')

            if sign == "!=":
                parent_a = dus.find(letter_1)
                parent_b = dus.find(letter_2)

                if parent_a == parent_b:
                    return False

        return True
