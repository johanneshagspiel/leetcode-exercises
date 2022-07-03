class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        def rec_mem(i, j, mem_dic):
            if (i == len(text1)) or (j == len(text2)):
                return 0

            elif (i, j) in mem_dic:
                return mem_dic[(i, j)]

            else:

                if text1[i] == text2[j]:
                    result = 1 + rec_mem(i + 1, j + 1, mem_dic)
                else:
                    result = max(rec_mem(i, j + 1, mem_dic), rec_mem(i + 1, j, mem_dic))

                mem_dic[(i, j)] = result
                return result

        return rec_mem(0, 0, {})
