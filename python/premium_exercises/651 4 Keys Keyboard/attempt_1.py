class Solution:
    def maxA(self, n: int) -> int:
        def rec_mem(input, num_A, selec_A, mem_dic):

            if input > n:
                return 0
            elif (num_A, selec_A, input) in mem_dic:
                return mem_dic[(num_A, selec_A, input)]
            else:
                option_1 = 1 + rec_mem(input + 1, num_A + 1, selec_A, mem_dic)

                option_2 = 0
                if num_A != selec_A:
                    option_2 = rec_mem(input + 1, num_A, num_A, mem_dic)

                option_3 = 0
                if selec_A != 0:
                    option_3 = rec_mem(input + 1, num_A + selec_A, selec_A, mem_dic)

                mem_dic[(num_A, selec_A, input)] = max(option_1, option_2, option_3)
                return mem_dic[(num_A, selec_A, input)]

        return rec_mem(0, 0, 0, {})
