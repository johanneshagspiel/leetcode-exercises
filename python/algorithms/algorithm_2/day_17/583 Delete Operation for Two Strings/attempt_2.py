class Solution:
    def minDistance(self, word1: str, word2: str) -> int:


        def rec_mem(i, j, mem_dic):

            key = str(i) + "-" + str(j)

            if i == len(word1) and j == 0:
                return len(word1)

            elif j == len(word2) and i == 0:
                return len(word2)

            elif i == len(word1) and j == len(word2):
                return 0
            
            elif key in mem_dic:
                return mem_dic[key]

            else:

                if word1[i] == word2[j]:
                    result = rec_mem(i+1, j+1, mem_dic)
                else:
                    result = 1 + min(rec_mem(i, j+1, mem_dic), rec_mem(i+1, j, mem_dic))

                mem_dic[key] = result
                return result


        return rec_mem(0, 0, {})