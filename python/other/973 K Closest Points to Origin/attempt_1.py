import math
import random
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:


        n = len(points)

        if k == n:
            return points


        def _calculate_distance_to_origin(x, y):
            return math.sqrt((x**2) + (y**2))


        def quick_select(left, right, k):

            if left < right:

                pivot_index = random.randint(left, right)

                final_index= partition(left, right, pivot_index)

                if final_index == k:
                    return

                elif k < final_index:
                    quick_select(left, final_index - 1, k)

                else:
                    quick_select(final_index + 1, right, k)


        def partition(left, right, pivot_index):
            target_distance = _calculate_distance_to_origin(points[pivot_index][0], points[pivot_index][1])

            points[right], points[pivot_index] = points[pivot_index], points[right]

            store_index = left

            for index in range(left, right):
                if _calculate_distance_to_origin(points[index][0], points[index][1]) < target_distance:
                    points[store_index], points[index] = points[index], points[store_index]
                    store_index += 1

            points[store_index], points[right] = points[right], points[store_index]

            return store_index


        quick_select(0, n-1, k)
        return points[:k]
