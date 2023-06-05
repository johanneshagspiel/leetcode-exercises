class Solution:
    def climbStairs(self, n: int) -> int:

        def rec_mem(index, mem_dic):
            if index == n:
                return 1
            elif index > n:
                return 0
            elif index in mem_dic:
                return mem_dic[index]
            else:
                res = rec_mem(index+1, mem_dic) + rec_mem(index+2, mem_dic)
                mem_dic[index] = res
                return res

        return rec_mem(0, {})
