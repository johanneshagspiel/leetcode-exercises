class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:


        def rec_palindrome(l, r, mem_dic):

            if l > r:
                return 0
            elif l == r:
                return 1

            elif (l, r) in mem_dic:
                return mem_dic[(l, r)]
            else:

                left_char = s[l]
                right_char = s[r]

                if left_char == right_char:
                    res =  2 + rec_palindrome(l + 1, r - 1, mem_dic)

                else:
                    op_1 = rec_palindrome(l + 1, r, mem_dic)
                    op_2 = rec_palindrome(l, r -1, mem_dic)
                    op_3 = rec_palindrome(l + 1, r - 1, mem_dic)

                    res = max(op_1, op_2, op_3)

                mem_dic[(l, r)] = res
                return res

        return rec_palindrome(0, len(s) - 1, {})