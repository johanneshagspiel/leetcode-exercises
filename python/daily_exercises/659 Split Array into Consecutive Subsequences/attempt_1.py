from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:

        bucket_size = max(nums) + 1

        buckets = [0] * (bucket_size)

        for num in nums:
            buckets[num] += 1

        subsequences = 0

        first_time = True

        while True:

            cur_len = 0
            found_start = False

            for index in range(bucket_size):
                if buckets[index] > 0:

                    if not found_start:
                        found_start = True
                        buckets[index] -= 1
                        cur_len += 1

                    else:
                        buckets[index] -= 1
                        cur_len += 1

                        if first_time:
                            if cur_len == 3:
                                first_time = False
                                break

                else:
                    if found_start:
                        break

            if cur_len == 0:
                break

            elif cur_len < 3:
                return False

            else:
                subsequences += 1

        if subsequences >= 2:
            return True
        else:
            return False
