import bisect


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:

        list = []
        result = []

        for num in obstacles:

            insertIdx = bisect.bisect_right(list, num)

            if insertIdx == len(list):
                list.append(num)
            else:
                list[insertIdx] = num

            result.append(insertIdx + 1)

        return result
