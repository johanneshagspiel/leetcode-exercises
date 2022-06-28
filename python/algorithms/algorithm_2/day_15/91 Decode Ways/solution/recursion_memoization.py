class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)

        def rec_mem(start_index, mem_dic):

            if start_index == n:
                return 1

            elif s[start_index] == '0':
                return 0

            elif start_index == (n - 1):
                return 1

            elif start_index in mem_dic:
                return mem_dic[start_index]

            else:

                ans = rec_mem(start_index+1, mem_dic)

                if int(s[start_index:(start_index+2)]) <= 26:
                    ans += rec_mem(start_index+2, mem_dic)

                mem_dic[start_index] = ans
                return ans

        return rec_mem(0, {})