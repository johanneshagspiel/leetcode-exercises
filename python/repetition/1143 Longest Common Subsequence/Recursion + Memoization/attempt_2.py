class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        len_1 = len(text1)
        len_2 = len(text2)

        def rec_mem(index_1, index_2, mem_dic):

            if index_1 == len_1 or index_2 == len_2:
                return 0

            elif (index_1, index_2) in mem_dic:
                return mem_dic[(index_1, index_2)]

            else:

                if text1[index_1] == text2[index_2]:
                    result = 1 + rec_mem(index_1+1, index_2+1, mem_dic)
                else:
                    result = max(rec_mem(index_1+1, index_2, mem_dic), rec_mem(index_1, index_2+1, mem_dic))

                mem_dic[(index_1, index_2)] = result
                return result

        return rec_mem(0, 0, {})
