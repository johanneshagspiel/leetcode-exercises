import math
class Solution:
    def isHappy(self, n: int) -> bool:

        n_2 = n

        while True:

            num_list = list(str(n))
            squared_sum = int(sum([pow(int(x), 2) for x in num_list]))

            if squared_sum == 1:
                return True

            num_list_1_1 = list(str(n_2))
            squared_sum_1_1 = int(sum([pow(int(x), 2) for x in num_list_1_1]))
            num_list_1_2 = list(str(squared_sum_1_1))
            squared_sum_2_1 = int(sum([pow(int(x), 2) for x in num_list_1_2]))

            if squared_sum == squared_sum_2_1:
                return False

            n = squared_sum
            n_2 = squared_sum_2_1
        