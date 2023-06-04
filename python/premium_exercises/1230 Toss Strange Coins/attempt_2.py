class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:

        mem_dic = {}

        def rec_mem(index, target, n):

            if target < 0:
                return 0

            elif index == n:
                if target == 0:
                    return 1
                else:
                    return 0

            elif (index, target) in mem_dic:
                return mem_dic[(index, target)]

            else:
                mem_dic[(index, target)] = rec_mem(index + 1, target - 1, n) * prob[index] + rec_mem(index + 1, target, n) * (1 - prob[index])
                return mem_dic[(index, target)]

        return rec_mem(0, target, len(prob))
