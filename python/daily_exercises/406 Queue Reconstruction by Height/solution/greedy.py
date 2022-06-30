import math
from typing import List
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:

        people.sort(key= lambda x: x[0])
        result_array = [(math.inf, 0) for _ in range(len(people))]

        for height, people_before in people:

            insert_position = 0
            for position in range(people_before):
                while result_array[insert_position][0] < height:
                    insert_position += 1
                insert_position += 1

            while result_array[insert_position][0] != math.inf:
                insert_position += 1

            result_array[insert_position] = (height, people_before)

        return result_array