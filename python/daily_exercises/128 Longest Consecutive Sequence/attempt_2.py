from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 0:
            return 0

        next_dic = {}
        previous_dic = {}
        seen_set = set()

        max_count = 1

        for num in nums:
            next_number = num + 1
            next_dic[num] = next_number
            previous_dic[next_number] = num

        for num in nums:

            if num not in seen_set:
                start_position = num
                while start_position in previous_dic:
                    start_position = previous_dic[start_position]

                seen_set.add(start_position)
                next_number = start_position + 1
                count = 1

                while next_number in next_dic:
                    seen_set.add(next_number)
                    count += 1
                    next_number = next_dic[next_number]

                max_count = max(count, max_count)

        return max_count
