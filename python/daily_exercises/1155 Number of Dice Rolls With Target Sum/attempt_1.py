class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        def rec_mem(num, cum_sum, mem_dic):

            if num == n and cum_sum == 0:
                return 1

            elif num == n and cum_sum != 0:
                return 0

            elif (num, cum_sum) in mem_dic:
                return mem_dic[(num, cum_sum)]

            else:

                ans = 0
                for pot in range(1, k + 1):
                    ans += rec_mem(num + 1, cum_sum - pot, mem_dic)

                ans = ans % (pow(10, 9) + 7)

                mem_dic[(num, cum_sum)] = ans
                return ans

        return rec_mem(0, target, {})
