import math
import random


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        n = len(points)

        if n == k:
            return points


        def calculate_distance(x, y ):
            return math.sqrt((x**2) + (y**2))

        def quick_select(left, right, k):

            if left < right:

                random_index = random.randint(left, right)

                pivot_index = partition(left, right, random_index)

                if pivot_index == k:
                    return

                elif k < pivot_index:
                    quick_select(left, pivot_index - 1, k)
                else:
                    quick_select(pivot_index + 1, right, k)


        def partition(left, right, pivot_index):
            target_distance = calculate_distance(points[pivot_index][0], points[pivot_index][1])

            points[right], points[pivot_index] = points[pivot_index], points[right]

            store_index = left

            for index in range(left, right):
                if calculate_distance(points[index][0], points[index][1]) < target_distance:
                    points[store_index], points[index] = points[index], points[store_index]
                    store_index += 1

            points[right], points[store_index] = points[store_index], points[right]

            return store_index


        quick_select(0, n -1, k)
        return points[:k]

