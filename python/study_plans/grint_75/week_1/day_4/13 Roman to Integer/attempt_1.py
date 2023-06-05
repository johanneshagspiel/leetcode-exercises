from typing import List

class Solution:
    def romanToInt(self, s: str) -> int:

        size_dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        prev_char = None
        result_int = 0

        for index, char in enumerate(s):
            current_value = size_dic[char]

            if index != 0:
                value_prev = size_dic[prev_char]

                if current_value > value_prev:
                    new_value = (current_value - value_prev) - value_prev
                    result_int += new_value
                else:
                    result_int += current_value
            else:
                result_int += current_value
            prev_char = char

        return result_int

if __name__ == '__main__':
    solution = Solution()
    s = "MCMXCIV"
    output = solution.romanToInt(s)
    print(output)