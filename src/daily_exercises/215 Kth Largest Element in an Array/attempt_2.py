import random
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def partition(pivot, left, right):
            pivot_value = nums[pivot]

            nums[pivot], nums[right] = nums[right], nums[pivot]

            store_index = left
            for index in range(left, right):
                if nums[index] < pivot_value:
                    nums[index], nums[store_index] = nums[store_index], nums[index]
                    store_index += 1

            nums[store_index], nums[right] = nums[right], nums[store_index]

            return store_index

        def select(left, right, k):

            if left == right:
                return nums[left]

            random_index = random.randint(left, right)
            pivot_index = partition(random_index, left, right)

            if pivot_index == k:
                return nums[pivot_index]
            elif pivot_index < k:
                return select(pivot_index + 1, right, k)
            else:
                return select(left, pivot_index - 1, k)

        return select(0, len(nums) - 1, len(nums) - k)
