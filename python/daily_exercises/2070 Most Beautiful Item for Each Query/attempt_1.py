class Solution(object):
    def maximumBeauty(self, items, queries):
        """
        :type items: List[List[int]]
        :type queries: List[int]
        :rtype: List[int]
        """

        items.sort(key=lambda x : x[0])

        max_beauty = items[0][1]
        for i in range(len(items)):
            max_beauty = max(max_beauty, items[i][1])
            items[i][1] = max_beauty

        res = []

        for query in queries:
            left = 0
            right = len(items) - 1
            found_max_beauty = 0

            while left <= right:
                mid = (left + right) // 2

                if items[mid][0] > query:
                    right = mid - 1
                else:
                    found_max_beauty = max(found_max_beauty, items[mid][1])
                    left = mid + 1

            res.append(found_max_beauty)

        return res
