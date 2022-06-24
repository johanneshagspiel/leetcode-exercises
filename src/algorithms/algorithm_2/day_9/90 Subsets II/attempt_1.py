import json
from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def backtrack(subset_size, first_index, current_list):

            if len(current_list) == subset_size:
                result_set.add(json.dumps(current_list[::]))

            for index in range(first_index, n):
                current_list.append(nums[index])
                backtrack(subset_size, index + 1, current_list)
                current_list.pop()

        result_set = set()
        n = len(nums)

        for subset_size in range(n + 1):
            backtrack(subset_size, 0, [])
        result_list = list(result_set)
        test = [json.loads(x) for x in result_list]

        return test
