import collections
import random


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequency_counter = collections.Counter(nums)
        unique_values = list(frequency_counter.keys())
        n = len(unique_values)


        def partition(left, right, pivot_index):
            target_frequency = frequency_counter[unique_values[pivot_index]]

            unique_values[right], unique_values[pivot_index] = unique_values[pivot_index], unique_values[right]

            store_index = left

            for index in range(left, right):
                if frequency_counter[unique_values[index]] < target_frequency:
                    unique_values[store_index], unique_values[index] = unique_values[index], unique_values[store_index]
                    store_index += 1

            unique_values[right], unique_values[store_index] = unique_values[store_index], unique_values[right]

            return store_index


        def quick_select(left, right, k_smallest):

            if left == right:
                return

            random_index = random.randint(left, right)
            pivot_index = partition(left, right, random_index)

            if pivot_index == k_smallest:
                return
            elif k_smallest < pivot_index:
                quick_select(left, pivot_index-1, k_smallest)
            else:
                quick_select(pivot_index+1, right, k_smallest)


        quick_select(0, n-1, n-k)
        return unique_values[n-k:]
