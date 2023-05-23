import collections
import random


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = collections.Counter(nums)
        unique = list(count.keys())
        def partition(left, right, pivot_index):

            pivot_frequency = count[unique[pivot_index]]

            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

            store_index = left

            for index in range(left, right):
                compare_freq = count[unique[index]]

                if compare_freq < pivot_frequency:
                    unique[store_index], unique[index] = unique[index], unique[store_index]
                    store_index += 1

            unique[store_index], unique[right] = unique[right], unique[store_index]
            return store_index

        def quick_select(left, right, nsmallest):

            if left == right:
                return

            pivot_index = random.randint(left, right)

            pivot_index = partition(left, right, pivot_index)

            if pivot_index == nsmallest:
                return

            elif nsmallest < pivot_index:
                quick_select(left, pivot_index - 1, nsmallest)
            else:
                quick_select(pivot_index + 1, right, nsmallest)

        n = len(unique)
        quick_select(0, n - 1, n-k)
        return unique[n-k:]
