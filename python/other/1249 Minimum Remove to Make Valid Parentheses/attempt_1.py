class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        open_par = 0
        closed_par = 0

        delete_index_list = []
        pot_open_list = []

        for index, letter in enumerate(s):
            if letter == '(':
                open_par += 1
                pot_open_list.append(index)

            elif letter == ')':
                if closed_par == open_par:
                    delete_index_list.append(index)
                else:
                    closed_par += 1
                    pot_open_list.pop()

        if len(pot_open_list) > 0:
            delete_index_list.extend(pot_open_list)

        delete_index_set = set(delete_index_list)

        result = []

        for index, char in enumerate(s):
            if index not in delete_index_set:
                result.append(char)

        return "".join(result)
