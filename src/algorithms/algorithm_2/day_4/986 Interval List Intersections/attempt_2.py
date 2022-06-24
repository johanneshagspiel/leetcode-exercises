from typing import List
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:

        i = 0
        j = 0

        len_a = len(A)
        len_b = len(B)

        output_list = []

        while i < len_a and j < len_b:
            low = max(A[i][0], B[j][0])
            high = min(A[i][1], B[j][1])

            if low <= high:
                output_list.append((low, high))

            if A[i][1] <= B[j][1]:
                i += 1
            else:
                j += 1

        return output_list
