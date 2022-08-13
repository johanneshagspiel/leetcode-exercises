from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.num_list = nums
        self.N = len(self.num_list)
        self.cum_sum = [0 for _ in range(self.N)]
        self.cum_sum[0] = self.num_list[0]

        for index in range(1, self.N):
            self.cum_sum[index] = self.cum_sum[index - 1] + self.num_list[index]

        self.correct_index = self.N - 1

    def update(self, index: int, val: int) -> None:
        self.num_list[index] = val

        self.correct_index = index - 1


    def sumRange(self, left: int, right: int) -> int:

        if right > self.correct_index:

            if self.correct_index == -1:
                self.cum_sum[0] = self.num_list[0]

                for index in range(self.correct_index + 1, right + 1):
                    self.cum_sum[index] = self.cum_sum[index - 1] + self.num_list[index]


            else:
                for index in range(self.correct_index, right + 1):
                    self.cum_sum[index] = self.cum_sum[index - 1] + self.num_list[index]

            self.correct_index = right



        if left == 0:
            res = self.cum_sum[right]

        else:
            res = self.cum_sum[right] - self.cum_sum[left - 1]

        return res

