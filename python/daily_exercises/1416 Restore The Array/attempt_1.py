class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:

        mod = pow(10, 9) + 7
        def rec_mem(start_index, current_index, mem_dic):

            if current_index > len(s):
                return 0
            else:

                cur_num = int(s[start_index:current_index])

                if cur_num < 1 or cur_num > k:
                    return 0
                else:

                    if start_index in mem_dic:
                        return mem_dic[start_index]

                    elif current_index == len(s):
                        return 1

                    else:
                        options = 0

                        options += rec_mem(current_index, current_index + 1, mem_dic)
                        options += rec_mem(start_index, current_index + 1, mem_dic)

                        mem_dic[start_index] = options

                        return options

        return rec_mem(0, 1, {}) % mod
