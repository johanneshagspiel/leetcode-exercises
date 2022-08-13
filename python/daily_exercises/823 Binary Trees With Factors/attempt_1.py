from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:

        arr.sort()
        res = 0

        com_dic = {}

        for index_1, num_1 in enumerate(arr):

            com_dic[num_1] = 1

            for index_2 in range(0, index_1):

                num_2 = arr[index_2]
                comp = num_1 / num_2

                if comp in com_dic:
                    com_dic[num_1] += com_dic[comp] * com_dic[num_2]

        for count in com_dic.values():
            res += count

        return res % ((10**9) + 7)
