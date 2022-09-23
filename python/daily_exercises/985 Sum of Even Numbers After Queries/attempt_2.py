from typing import List


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        even_sum = 0

        for num in nums:
            if num % 2 == 0:
                even_sum += num

        res = []

        for amount, index in queries:
            begin_amount = nums[index]
            start_even = begin_amount % 2 == 0

            end_amount = begin_amount + amount
            end_even = end_amount % 2 == 0

            if start_even and end_even:
                even_sum += amount

            elif start_even and not end_even:
                even_sum -= begin_amount

            elif not start_even and end_even:
                even_sum += end_amount

            nums[index] = end_amount

            res.append(even_sum)

        return res
