from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        number_dic = {}

        for number in nums:

            if number in number_dic:
                return True
            else:
                number_dic[number] = True

        return False
