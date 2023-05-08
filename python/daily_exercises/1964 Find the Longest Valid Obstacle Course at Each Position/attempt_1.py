class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:

        def determineObstacleCourse(compareNum, memList):

            notFound = True
            finalCount = 1

            for index in range(len(memList) -1, -1, -1):
                num, count = memList[index]

                if num <= compareNum:
                    memList.append((compareNum, count + 1))
                    finalCount = count + 1
                    notFound = False
                    break

            if notFound:
                memList.append((compareNum, 1))

            memList.sort(key = lambda x: x[1])
            return finalCount

        result = []
        result.append(1)
        memList = []
        memList.append((obstacles[0], 1))

        for i in range(1, len(obstacles)):
            result.append(determineObstacleCourse(obstacles[i], memList))

        return result
