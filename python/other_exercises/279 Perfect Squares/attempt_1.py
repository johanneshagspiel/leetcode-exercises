import math


class Solution:
    def numSquares(self, n: int) -> int:

        def rec_mem(num, mem_dic):

            sqrt = math.sqrt(num)

            if sqrt % 1 == 0:
                return 1

            elif num in mem_dic:
                return mem_dic[(num)]

            else:

                options = []

                for subtraction in (i**2 for i in range(int(sqrt) + 1, -1, -1)):
                    res = rec_mem(subtraction, mem_dic) + rec_mem(num - subtraction, mem_dic)
                    options.append(res)

                min_res = min(options)
                mem_dic[(num)] = min_res
                return min_res

        return rec_mem(n, {})
