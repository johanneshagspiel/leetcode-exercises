from typing import List


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:


        even_sum = 0

        for num in nums:
            if num % 2 == 0:
                even_sum += num

        res = []

        for value, index in queries:
            to_change_num = nums[index]
            start_even = to_change_num % 2 == 0

            changed_num = to_change_num + value
            end_even = changed_num % 2 == 0

            if start_even and not end_even:
                even_sum -= to_change_num

            elif not start_even and end_even:
                even_sum += changed_num

            elif start_even and end_even:
                even_sum += value

            nums[index] = changed_num

            res.append(even_sum)

        return res




