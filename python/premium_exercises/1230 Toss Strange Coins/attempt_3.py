class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:

        n = len(prob)

        def rec_mem(index, heads_needed, mem_dic):

            if heads_needed < 0:
                return 0

            elif index == n:
                if heads_needed == 0:
                    return 1
                else:
                    return 0

            elif (index, heads_needed) in mem_dic:
                return mem_dic[(index, heads_needed)]

            else:
                option_1 = prob[index] * rec_mem(index + 1, heads_needed - 1, mem_dic)
                option_2 = (1 - prob[index]) * rec_mem(index + 1, heads_needed, mem_dic)

                mem_dic[(index, heads_needed)] = option_1 + option_2
                return mem_dic[(index, heads_needed)]

        return rec_mem(0, target, {})
