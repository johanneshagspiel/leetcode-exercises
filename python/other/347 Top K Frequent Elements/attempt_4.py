import collections
import random


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequency_counter = collections.Counter(nums)
        unique = list(frequency_counter.keys())
        n = len(unique)


        def quick_select(left, right, k_smallest):

            if left == right:
                return

            pivot_index = random.randint(left, right)

            final_index_position = lomutso_partition(left, right, pivot_index)

            if final_index_position == k_smallest:
                return
            elif k_smallest < final_index_position:
                quick_select(left, final_index_position - 1, k_smallest)
            else:
                quick_select(final_index_position + 1, right, k_smallest)



        def lomutso_partition(left, right, pivot_index):
            target_frequency = frequency_counter[unique[pivot_index]]

            unique[right], unique[pivot_index] = unique[pivot_index], unique[right]

            store_index = left

            for index in range(left, right):
                if frequency_counter[unique[index]] < target_frequency:
                    unique[index], unique[store_index] = unique[store_index], unique[index]
                    store_index += 1

            unique[right], unique[store_index] = unique[store_index], unique[right]

            return store_index



        quick_select(0, n-1, n-k)
        return unique[(n-k):]
