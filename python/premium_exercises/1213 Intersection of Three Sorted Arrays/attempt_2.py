
class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """

        pointer_1 = 0
        pointer_2 = 0
        pointer_3 = 0

        res = []
        while pointer_1 < len(arr1):
            num_1 = arr1[pointer_1]

            while pointer_2 < len(arr2) and arr2[pointer_2] < num_1:
                pointer_2 += 1

            if pointer_2 == len(arr2):
                return res

            while pointer_3 < len(arr3) and arr3[pointer_3] < num_1:
                pointer_3 += 1

            if pointer_3 == len(arr3):
                return res

            if num_1 == arr2[pointer_2] and num_1 == arr3[pointer_3]:
                res.append(num_1)

            pointer_1 += 1

        return res
