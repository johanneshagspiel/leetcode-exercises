import collections
from typing import List


class DUS:

    def __init__(self):
        self.parents = [0 for _ in range(26)]
        self.rank = [0 for _ in range(26)]


    def find(self, a):

        if self.parents[a] != a:
            self.parents[a] = self.find(self.parents[a])

        return self.parents[a]


    def union(self, a, b):

        parent_a = self.find(a)
        parent_b = self.find(b)

        if parent_a == parent_b:
            return False
        else:
            rank_p_a = self.rank[parent_a]
            rank_p_b = self.rank[parent_b]

            if rank_p_b > rank_p_a:
                self.parents[parent_a] = parent_b
                self.rank[parent_b] += 1

            elif rank_p_a > rank_p_b:
                self.parents[parent_b] = parent_a
                self.rank[parent_a] += 1

            else:
                self.parents[parent_b] = parent_a
                self.rank[parent_a] += 1

            return True



class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        dus = DUS()

        un_equality_list = []

        for equation in equations:
            letter_1 = ord(equation[0]) - ord('a')
            sign = equation[1:3]
            letter_2 = ord(equation[3]) - ord('a')

            if sign == "==":
                dus.union(letter_1, letter_2)

            else:
                un_equality_list.append((letter_1, letter_2))



        for letter_1, letter_2 in un_equality_list:
            parent_1 = dus.find(letter_1)
            parent_2 = dus.find(letter_2)

            if parent_1 == parent_2:
                return False

        return True
