from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        binary_mask = sum([x.isalpha() for x in s])
        result_list = []

        for bits in range(1 << binary_mask):
            b = 0
            word = []

            for letter in s:
                if letter.isalpha():
                    if (bits >> b) & 1:
                        word.append(letter.upper())
                    else:
                        word.append(letter.lower())

                    b += 1
                else:
                    word.append(letter)

            result_list.append("".join(word))

        return result_list
