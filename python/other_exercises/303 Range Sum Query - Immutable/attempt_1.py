from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.result_dic = {}

    def sumRange(self, left: int, right: int) -> int:
        if right in self.result_dic:
            right_cum = self.result_dic[right]
        else:
            right_cum = sum(self.nums[:right+1])
            self.result_dic[right] = right_cum

        one_to_left = left - 1
        if one_to_left < 0:
            left_cum = 0
        elif one_to_left in self.result_dic:
            left_cum = self.result_dic[one_to_left]
        else:
            left_cum = sum(self.nums[:left])
            self.result_dic[one_to_left] = left_cum

        return right_cum - left_cum

