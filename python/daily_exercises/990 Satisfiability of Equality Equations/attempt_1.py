import collections
from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        equality_dic = collections.defaultdict(set)
        un_equality_list = []

        for equation in equations:
            letter_1 = equation[0]
            sign = equation[1:3]
            letter_2 = equation[3]

            if sign == "==":
                equality_dic[letter_1].add(letter_2)
                equality_dic[letter_2].add(letter_1)
            else:
                equality_dic[letter_1] = set()
                equality_dic[letter_2] = set()
                un_equality_list.append((letter_1, letter_2))

        assigned_value_dic = collections.defaultdict(int)
        current_value = 1

        for letter, corresponding_letter_set in equality_dic.items():

            if letter not in assigned_value_dic:
                assigned_value_dic[letter] = current_value

                for corresponding_letter in corresponding_letter_set:
                    if corresponding_letter not in assigned_value_dic:
                        assigned_value_dic[corresponding_letter] = current_value
                    else:
                        return False

                current_value += 1


        for letter_1, letter_2 in un_equality_list:
            if assigned_value_dic[letter_1] == assigned_value_dic[letter_2]:
                return False

        return True

