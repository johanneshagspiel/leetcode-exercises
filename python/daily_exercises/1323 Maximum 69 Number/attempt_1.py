class Solution:
    def maximum69Number(self, num: int) -> int:

        num_list = list(str(num))

        first_six_index = len(num_list) + 1

        for index, ind_num in enumerate(num_list):

            if ind_num == '6':
                first_six_index = min(first_six_index, index)

        if first_six_index != len(num_list) + 1:
            num_list[first_six_index] = '9'

            return int("".join(num_list))

        else:
            return num