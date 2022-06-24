from typing import List
from itertools import product


class Solution:

    def hasAllCodes(self, s: str, k: int) -> bool:

        all_possible_combinations = pow(2, k)
        all_possible_combinations_dic = {}

        start_index = 0
        end_index = start_index + k

        if end_index > len(s):
            return False


        while True:
            substring = s[start_index:end_index]
            if substring not in all_possible_combinations_dic:

                all_possible_combinations_dic[substring] = True

                if len(all_possible_combinations_dic) == all_possible_combinations:
                    return True

            start_index += 1
            end_index += 1

            if end_index > len(s):
                return False



if __name__ == '__main__':
    solution = Solution()

    s = "011111011101111000010111100001011010010011010100100111101101011010111011011100110001011010001000100110010000101010000000111000010001011001110011100000100101000011110010000101001111110001001010111000011010011111111100011110000111110101101"
    k = 18
    output_1 = solution.hasAllCodes(s, k)
    expected_1 = 16

    print(output_1)