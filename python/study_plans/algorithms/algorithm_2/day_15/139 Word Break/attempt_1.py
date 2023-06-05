from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)

        if n == 1:
            return s[0] in wordDict

        def rec(start_index, mem_dic):

            if start_index == n:
                return True

            elif start_index in mem_dic:
                return mem_dic[start_index]

            else:

                for end_index in range(start_index, n):
                    sub_string = s[start_index:(end_index + 1)]

                    if sub_string in wordDict and rec(end_index + 1, mem_dic):
                        mem_dic[start_index] = True
                        return True

                mem_dic[start_index] = False
                return False

        return rec(0, {})

