from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        letter_dic = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }
        result = []
        n = len(digits)

        def back_tracking(current_index, current_list):

            if current_index == n:
                if len(current_list) > 0:
                    result.append("".join(current_list))
                return

            else:

                current_number = digits[current_index]
                letter_list = letter_dic[current_number]

                for letter in letter_list:

                    current_list.append(letter)
                    back_tracking(current_index+1, current_list)
                    current_list.pop()

        back_tracking(0, [])
        return result


