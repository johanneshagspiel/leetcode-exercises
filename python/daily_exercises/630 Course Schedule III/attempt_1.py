from typing import List
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:

        self.max_courses_count = 0

        courses.sort(key= lambda x: x[1])

        self.back_track(courses, 0, 0)

        return self.max_courses_count

    def back_track(self, courses, start_day, courses_count):

        self.max_courses_count = max(self.max_courses_count, courses_count)

        if len(courses) == 0:
            return
        else:
            first_duration, first_last_day = courses[0]

            if (start_day + first_duration) > (first_last_day):
                return
            else:
                for index, (duration, last_day) in enumerate(courses):
                    finish_day = start_day + duration
                    if finish_day <= last_day:
                        start_day += duration
                        courses_count += 1
                        temp_courses = courses.pop(index)

                        self.back_track(courses, start_day, courses_count)

                        courses.insert(index, temp_courses)
                        start_day -= duration
                        courses_count -= 1
                    else:
                        return
