import collections
import random


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequency_counter = collections.Counter(nums)
        unique_values = list(frequency_counter.keys())
        N = len(unique_values)


        def quick_select(left, right, k_smallest):

            if left == right:
                return

            pivot_index = random.randint(left, right)

            final_index = partition_algorithm(left, right, pivot_index)

            if final_index == k_smallest:
                return
            elif k_smallest < final_index:
                quick_select(left, final_index - 1, k_smallest)
            else:
                quick_select(final_index+1, right, k_smallest)


        def partition_algorithm(left, right, pivot_index):

            target_frequency = frequency_counter[unique_values[pivot_index]]

            unique_values[pivot_index], unique_values[right] = unique_values[right], unique_values[pivot_index]

            store_index = left

            for index in range(left, right):
                if frequency_counter[unique_values[index]] < target_frequency:
                    unique_values[store_index], unique_values[index] = unique_values[index], unique_values[store_index]
                    store_index += 1

            unique_values[store_index], unique_values[right] = unique_values[right], unique_values[store_index]

            return store_index


        quick_select(0, N - 1, N - k)
        return unique_values[(N - k):]


