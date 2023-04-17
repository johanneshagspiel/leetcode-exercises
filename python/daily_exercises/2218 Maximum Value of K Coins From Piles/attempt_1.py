class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:

        selected_index = [0 for _ in range(len(piles))]

        def rec_mem(coin_remaining, index_list, mem_dic):

            mem_key = "_".join([str(x) for x in index_list])

            if coin_remaining == 0:
                return 0
            else:
                if (coin_remaining, mem_key) in mem_dic:
                    return mem_dic[(coin_remaining, mem_key)]

                else:

                    options = []

                    for pile in range(len(piles)):
                        max_index = len(piles[pile])
                        cur_index = index_list[pile]

                        if cur_index < max_index:
                            index_list[pile] += 1
                            new_op = piles[pile][cur_index] + rec_mem(coin_remaining - 1,
                                                                      index_list,
                                                                      mem_dic)
                            index_list[pile] -= 1

                            options.append(new_op)

                    max_option = max(options)

                    mem_dic[(coin_remaining, mem_key)] = max_option
                    return max_option

        return rec_mem(k, selected_index, {})
