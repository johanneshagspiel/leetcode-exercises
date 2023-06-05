from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        N = len(s)
        result_list = []

        def letter_check(index, char_list):

            if index == N:
                result_list.append("".join(char_list))

            else:
                if char_list[index].isalpha():
                    char_list[index] = char_list[index].upper()
                    letter_check(index+1, char_list)

                    char_list[index] = char_list[index].lower()
                    letter_check(index+1, char_list)
                else:
                    letter_check(index+1, char_list)


        letter_check(0, list(s))
        return result_list
