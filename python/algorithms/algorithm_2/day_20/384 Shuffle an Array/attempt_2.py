import random
from typing import List

class Solution:

    def __init__(self, nums: List[int]):
        self.working_list = nums
        self.original_list = nums[::]

    def reset(self) -> List[int]:
        return self.original_list

    def shuffle(self) -> List[int]:
        for index in range(len(self.working_list)):
            change_position = random.randint(0, index)

            self.working_list[index], self.working_list[change_position] = self.working_list[change_position], \
                                                                           self.working_list[index]

        return self.working_list