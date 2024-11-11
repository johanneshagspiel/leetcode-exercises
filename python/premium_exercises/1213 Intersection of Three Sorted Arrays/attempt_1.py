from collections import defaultdict


class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """

        num_count = defaultdict(int)

        for num2 in arr2:
            num_count[num2] += 1

        for num3 in arr3:
            num_count[num3] += 1

        res = []

        for num1 in arr1:
            count = num_count[num1]
            if count == 2:
                res.append(num1)

        return res
