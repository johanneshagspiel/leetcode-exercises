from typing import List


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:

        n = len(courses)
        courses.sort(key = lambda x: x[1])

        def rec(start_course, start_time, memo_dic):

            if start_course == n:
                return 0

            elif start_course in memo_dic and start_time in memo_dic[start_course]:
                return memo_dic[start_course][start_time]

            else:
                taken = 0
                if start_time + courses[start_course][0] <= courses[start_course][1]:
                    taken = 1 + rec(start_course + 1, start_time + courses[start_course][0], memo_dic)
                not_taken = rec(start_course + 1, start_time, memo_dic)

                if start_course not in memo_dic:
                    memo_dic[start_course] = {}
                memo_dic[start_course][start_time] = max(taken, not_taken)
                return memo_dic[start_course][start_time]

        return rec(0, 0, {})