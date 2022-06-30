class Solution:
    def integerBreak(self, n: int) -> int:

        def rec_mem(remaining, cum_mul):

            if remaining == 0:
                return cum_mul

            else:

                result_list = []
                for number in range(1, remaining):
                    result_list.append(rec_mem(remaining-number, cum_mul*number))

                res = max(result_list)
                return res

        return rec_mem(10, 1)








