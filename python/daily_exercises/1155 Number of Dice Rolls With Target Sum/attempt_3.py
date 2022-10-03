class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        def rec_mem(dice_number, cum_sum, mem_dic):

            if dice_number == n and cum_sum == target:
                return 1

            elif dice_number == n and cum_sum != target:
                return 0

            elif (dice_number, cum_sum) in mem_dic:
                return mem_dic[(dice_number, cum_sum)]

            else:

                res = 0

                for addition in range(1, k + 1):
                    res += rec_mem(dice_number + 1, cum_sum + addition, mem_dic)

                res = res % (pow(10, 9) + 7)

                mem_dic[(dice_number, cum_sum)] = res

                return res

        return rec_mem(0, 0, {})

