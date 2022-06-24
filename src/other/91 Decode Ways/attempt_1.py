import json
from string import ascii_uppercase

class Solution:
    def numDecodings(self, s: str) -> int:
        # conversion_dic = {}
        # for number, letter in enumerate(ascii_uppercase):
        #     conversion_dic[number + 1] = letter
        return self.numDecodings_Helper("", s, {})

    def numDecodings_Helper(self, digit_string, remainder, memo_dic):

        if len(digit_string) > 0:
            if digit_string[0] == '0' or int(digit_string) > 26:
                return 0

            else:
                new_key = digit_string + "_" + remainder
                if new_key in memo_dic:
                    return memo_dic[new_key]
                else:

                    if len(remainder) == 0:
                        conversion_options = 1
                    else:
                        if len(remainder) == 1:
                            conversion_options = self.numDecodings_Helper(remainder, "", memo_dic)
                        else:
                            digit_string_1 = remainder[:1]
                            remainder_1 = remainder[1:]

                            digit_string_2 = remainder[:2]
                            remainder_2 = remainder[2:]

                            conversion_options = self.numDecodings_Helper(digit_string_1, remainder_1, memo_dic) + self.numDecodings_Helper(digit_string_2, remainder_2, memo_dic)

                    memo_dic[new_key] = conversion_options
                    return conversion_options

        else:
            new_key = digit_string + "_" + remainder
            if new_key in memo_dic:
                return memo_dic[new_key]
            else:
                if len(remainder) == 0:
                    conversion_options = 0
                else:
                    if len(remainder) == 1:
                        conversion_options = self.numDecodings_Helper(remainder, "", memo_dic)
                    else:
                        digit_string_1 = remainder[:1]
                        remainder_1 = remainder[1:]

                        digit_string_2 = remainder[:2]
                        remainder_2 = remainder[2:]

                        conversion_options = self.numDecodings_Helper(digit_string_1, remainder_1 , memo_dic) + self.numDecodings_Helper(digit_string_2, remainder_2 , memo_dic)

                memo_dic[new_key] = conversion_options
                return conversion_options


if __name__ == '__main__':
    solution = Solution()

    input_1 = "226"
    output_1 = solution.numDecodings(input_1)
    expected_1 = 3

    print(output_1)
