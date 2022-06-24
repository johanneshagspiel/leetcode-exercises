import itertools
import json


class Solution:
    def climbStairs(self, n: int) -> int:
        two_steps_taken = 0
        one_steps_taken = n
        total_combinations = 0

        while one_steps_taken >= 0:
            combination_list = []

            for two_steps in range(0, two_steps_taken):
                combination_list.append(2)

            for one_steps in range(0, one_steps_taken):
                combination_list.append(1)

            two_steps_taken += 1
            one_steps_taken = n - (2 * two_steps_taken)

            total_combinations += 1

        return total_combinations

if __name__ == '__main__':

    # test = [1, 1, 1, 2]
    # print(json.dumps(list(itertools.product(test, repeat=4))))

    solution = Solution()
    input_1 = 38
    output = solution.climbStairs(input_1)
    print(output)