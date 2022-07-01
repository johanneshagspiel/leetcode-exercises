import copy
import random
from typing import List
class Solution:

    def __init__(self, nums: List[int]):
        self.initial_list = nums

    def reset(self) -> List[int]:
        return self.initial_list

    def shuffle(self) -> List[int]:

        end_position = len(self.initial_list) -1
        selection_list = copy.deepcopy(self.initial_list)
        result_list = []

        while end_position >=0:
            random_position = random.randint(0, end_position)
            insert_value = selection_list.pop(random_position)
            result_list.append(insert_value)
            end_position -= 1

        return result_list


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()