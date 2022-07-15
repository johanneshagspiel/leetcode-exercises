from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        result_list =[]

        N = len(s)

        def rec(index, char_list):

            if index == N:
                result_list.append("".join(char_list))

            else:
                if char_list[index].isalpha():
                    char_list[index] = char_list[index].upper()
                    rec(index+1, char_list)

                    char_list[index] = char_list[index].lower()
                    rec(index+1, char_list)
                else:
                    rec(index+1, char_list)

        rec(0, list(s))
        return result_list
