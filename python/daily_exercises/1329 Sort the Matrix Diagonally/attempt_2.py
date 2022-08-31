import collections
import heapq
from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:

        columns = len(mat)
        rows = len(mat[0])

        diagonal_dic = collections.defaultdict(list)

        for column in range(columns):
            for row in range(rows):
                diagonal_dic[row - column].append(mat[column][row])

        for diagonal_list in diagonal_dic.values():
            heapq.heapify(diagonal_list)

        for column in range(columns):
            for row in range(rows):
                mat[column][row] = heapq.heappop(diagonal_dic[row - column])

        return mat

