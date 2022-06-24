from typing import List

class Solution:
    def romanToInt(self, s: str) -> int:


        string_list = list(s)

        size_dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        result_int = 0
        index = 0

        while index < len(s):

            current_value = size_dic[string_list[index]]
            if index + 1 < len(s):
                next_value = size_dic[string_list[index + 1]]
                if next_value > current_value:
                    result_int += next_value - current_value
                    index += 2
                else:
                    result_int += current_value
                    index += 1
            else:
                result_int += current_value
                index += 1

        return result_int


if __name__ == '__main__':
    solution = Solution()
    s = "MCMXCIV"
    output = solution.romanToInt(s)
    print(output)