class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        def rec_mem(i, j, mem_dic):

            key = str(i) + "_" + str(j)

            if (i < 0) and (j < 0):
                return 0

            elif (i < 0):
                return j + 1

            elif (j < 0):
                return i + 1

            elif key in mem_dic:
                return mem_dic[key]

            else:

                if word1[i] == word2[j]:
                    result = rec_mem(i - 1, j - 1, mem_dic)
                else:
                    result = 1 + min(rec_mem(i - 1, j, mem_dic), rec_mem(i, j - 1, mem_dic))

                mem_dic[key] = result
                return result

        return rec_mem(len(word1) - 1, len(word2) - 1, {})