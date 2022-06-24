import random
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        def partition(left, right, pivot):
            pivot_value = nums[pivot]

            nums[right], nums[pivot] = nums[pivot], nums[right]

            store_index = left
            for index in range(left, right):
                if nums[index] < pivot_value:
                    nums[index], nums[store_index] = nums[store_index], nums[index]
                    store_index += 1

            nums[right], nums[store_index] = nums[store_index], nums[right]

            return store_index

        def search(left, right, k_smallest):

            if left == right:
                return nums[left]

            random_index = random.randint(left, right)
            pivot_index = partition(left, right, random_index)

            if pivot_index == k_smallest:
                return nums[k_smallest]
            elif k_smallest < pivot_index:
                return search(left, pivot_index - 1, k_smallest)
            else:
                return search(pivot_index + 1, right, k_smallest)

        return search(0, len(nums) - 1, len(nums) - k)
