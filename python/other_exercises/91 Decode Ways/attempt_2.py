class Solution:
    def numDecodings(self, s: str) -> int:

        res = 0

        n = len(s)

        def rec_mem(index, mem_dic):

            nonlocal res

            if index >= n:
                return 1

            elif index in mem_dic:
                return mem_dic[index]

            else:
                current_num = int(s[index])

                if index == (n - 1):

                    if current_num != 0:
                        return rec_mem(index + 1, mem_dic)
                    else:
                        return 0

                else:

                    next_num = int(s[index + 1])

                    res_1 = 0
                    res_2 = 0

                    if next_num == 0:

                        if current_num != 0:
                            res_1 = rec_mem(index + 2, mem_dic)
                        else:
                            return 0

                    elif current_num >= 3:
                        res_1 = rec_mem(index + 1, mem_dic)

                    elif current_num == 1:
                        res_1 = rec_mem(index + 2, mem_dic)
                        res_2 = rec_mem(index + 1, mem_dic)

                    elif current_num == 2:
                        if next_num <= 6:
                            res_1 = rec_mem(index + 2, mem_dic)
                        res_2 = rec_mem(index + 1, mem_dic)

                    mem_dic[index] = res_1 + res_2
                    return mem_dic[index]

        return rec_mem(0, {})
