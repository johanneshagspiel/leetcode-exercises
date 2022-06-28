class Solution:
    def numDecodings(self, s: str) -> int:

        if s[0] == '0':
            return 0

        n = len(s)
        self.n_decodings = 1


        def rec(start_index, mem_dic):

            if start_index in mem_dic:
                return mem_dic[start_index]

            elif start_index < (n -1):
                number = s[start_index]
                next_number = int(s[start_index + 1])

                if number == '0':
                    result = 0

                elif number == '1':
                    if next_number == 0:
                        result = rec(start_index + 2, mem_dic)
                    else:
                        result = rec(start_index + 1, mem_dic) + rec(start_index + 2, mem_dic)

                elif number == '2':
                    if next_number == 0:
                        result = rec(start_index + 2, mem_dic)
                    elif next_number <= 6:
                        result = rec(start_index + 1, mem_dic) + rec(start_index + 2, mem_dic)

                    else:
                        result = rec(start_index + 1, mem_dic)

                else:
                    result = rec(start_index + 1, mem_dic)

                mem_dic[start_index] = result
                return result

            else:
                if start_index > (n - 1):
                    return
                elif s[n-1] == '0':
                    return 0
                else:
                    return 1

        return rec(0, {})
