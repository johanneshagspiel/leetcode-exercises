import collections
from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        letter_set = set()

        un_equality_list = []
        equality_list = []

        for equation in equations:
            letter_1 = equation[0]
            sign = equation[1:3]
            letter_2 = equation[3]

            letter_set.add(letter_1)
            letter_set.add(letter_2)

            if sign == "!=":
                un_equality_list.append((letter_1, letter_2))
            else:
                equality_list.append((letter_1, letter_2))

        assigned_value_dic = collections.defaultdict(int)

        current_value = 1

        for letter_1, letter_2 in equality_list:
            letter_1_val = assigned_value_dic[letter_1]
            letter_2_val = assigned_value_dic[letter_2]

            if letter_1_val != 0 and letter_2_val != 0 and letter_1_val != letter_2_val:
                return False

            if letter_1_val != 0 and letter_2_val != 0 and letter_1_val == letter_2_val:
                continue

            elif letter_1_val != 0 and letter_2_val == 0:
                assigned_value_dic[letter_2] = letter_1_val

            elif letter_1_val == 0 and letter_2_val != 0:
                assigned_value_dic[letter_1] = letter_2_val

            else:
                assigned_value_dic[letter_1] = current_value
                assigned_value_dic[letter_2] = current_value

                current_value += 1

        for letter in letter_set:
            letter_val = assigned_value_dic[letter]

            if letter_val == 0:
                assigned_value_dic[letter] = current_value
                current_value += 1

        for letter_1, letter_2 in un_equality_list:
            letter_1_val = assigned_value_dic[letter_1]
            letter_2_val = assigned_value_dic[letter_2]

            if letter_1_val == letter_2_val:
                return False

        return True
        