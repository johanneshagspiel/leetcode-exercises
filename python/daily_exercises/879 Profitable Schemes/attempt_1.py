class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:

        mod = pow(10, 9) + 7

        profit = [x for _, x in sorted(zip(group, profit), key=lambda pair: pair[0], reverse=True)]
        group = [x for x, _ in sorted(zip(group, profit), key= lambda x: x[0], reverse=True)]

        def rec_mem(cur_ind, in_profit, in_group, rec_dic):

            if in_group == 0:
                if in_profit <= 0:
                    return 1
                else:
                    return 0

            elif in_group < 0:
                return 0

            elif cur_ind == len(profit):
                if in_profit <= 0:
                    return 1
                else:
                    return 0

            elif (cur_ind, in_profit, in_group) in rec_dic:
                return rec_dic[(cur_ind, in_profit, in_group)]

            else:

                options = 0

                cur_thief = group[cur_ind]
                cur_profit = profit[cur_ind]

                options += rec_mem(cur_ind + 1, in_profit - cur_profit, in_group - cur_thief, rec_dic)
                options += rec_mem(cur_ind + 1, in_profit, in_group, rec_dic)

                options = options % mod

                rec_dic[(cur_ind, in_profit, in_group)] = options
                return options

        return rec_mem(0, minProfit, n, {})
