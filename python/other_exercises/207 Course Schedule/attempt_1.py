import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if len(prerequisites) == 0:
            return True

        course_dic = collections.defaultdict(list)

        for course, prerequisite_course in prerequisites:
            course_dic[course].append(prerequisite_course)

        first_course = prerequisites[0][0]
        stack = []
        stack.append(first_course)
        required_courses_set = set()

        done_courses = 0

        while stack:
            current_course = stack.pop()
            done_courses += 1

            required_courses = course_dic[current_course]

            for required_course in required_courses:
                if required_course in required_courses_set:
                    return False
                else:
                    required_courses_set.add(required_course)
                    stack.append(required_course)

        return done_courses == numCourses
