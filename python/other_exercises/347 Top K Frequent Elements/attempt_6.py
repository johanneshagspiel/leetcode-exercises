import collections
import random


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequency_counter = collections.Counter(nums)
        unique_values = list(frequency_counter.keys())
        n = len(unique_values)


        def quick_select(left, right, amount_sorted):

            if left < right:
                random_index = random.randint(left, right)

                pivot_index = partition(left, right, random_index)

                if pivot_index == amount_sorted:
                    return

                elif amount_sorted < pivot_index:
                    quick_select(left, pivot_index - 1, amount_sorted)

                else:
                    quick_select(pivot_index + 1, right, amount_sorted)


        def partition(left, right, parition_index):

            target_frequency = frequency_counter[unique_values[parition_index]]

            unique_values[right], unique_values[parition_index] = unique_values[parition_index], unique_values[right]

            store_index = left

            for index in range(left, right):
                if frequency_counter[unique_values[index]] < target_frequency:
                    unique_values[store_index], unique_values[index] = unique_values[index], unique_values[store_index]
                    store_index += 1

            unique_values[right], unique_values[store_index] = unique_values[store_index], unique_values[right]

            return store_index


        quick_select(0, n-1, n-k)
        return unique_values[n-k:]
