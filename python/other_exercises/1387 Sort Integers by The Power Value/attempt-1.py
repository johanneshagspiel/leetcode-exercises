import heapq


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        def rec_mem(n, mem_dic):

            steps = 0

            while n != 1:
                if n in mem_dic:
                    return steps + mem_dic[n]
                else:
                    steps += 1
                    n = fn(n)

            return steps

        def fn(n):
            if n % 2 == 0:
                return n / 2
            else:
                return 3 * n + 1

        mem_dic = {}
        result_list = []

        for num in range(lo, hi + 1):
            result = rec_mem(num, mem_dic)
            mem_dic[num] = result
            result_list.append((result, num))

        result_list.sort(key= lambda x:x[0])

        return result_list[k][1]
