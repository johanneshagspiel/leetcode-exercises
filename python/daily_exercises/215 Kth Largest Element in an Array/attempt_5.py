import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def partition(left, right, partition_index):
            target_value = nums[partition_index]

            nums[right], nums[partition_index] = nums[partition_index], nums[right]

            store_index = left

            for index in range(left, right):
                if nums[index] < target_value:
                    nums[index], nums[store_index] = nums[store_index], nums[index]
                    store_index += 1

            nums[right], nums[store_index] = nums[store_index], nums[right]

            return store_index


        def select(left, right, k):

            if left == right:
                return nums[left]

            random_index = random.randint(left, right)

            pivot_index = partition(left, right, random_index)

            if pivot_index == k:
                return nums[k]

            elif pivot_index < k:
                return select(pivot_index + 1, right, k)

            else:
                return select(left, pivot_index - 1, k)

        return select(0, len(nums) - 1, len(nums) - k)