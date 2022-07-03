import math

class Solution:
    def isHappy(self, n: int) -> bool:

        n_2 = n

        while True:

            num_list = list(str(n))
            square_sum = int(sum([math.pow(int(x), 2) for x in num_list]))

            if square_sum == 1:
                return True

            num_list_1_2 = list((str(n_2)))
            square_sum_1_2 = int(sum([math.pow(int(x), 2) for x in num_list_1_2]))
            num_list_2_2 = list((str(square_sum_1_2)))
            square_sum_2_2 = int(sum([math.pow(int(x), 2) for x in num_list_2_2]))

            if square_sum == square_sum_2_2:
                return False

            n = square_sum
            n_2 = square_sum_2_2