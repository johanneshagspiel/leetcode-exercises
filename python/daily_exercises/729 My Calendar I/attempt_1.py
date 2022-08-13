class MyCalendar:

    def __init__(self):
        self.booked_slots_dic = {}

    def book(self, start: int, end: int) -> bool:

        not_found = True

        for time in range(start, end):
            if time in self.booked_slots_dic:
                not_found = False
                break

        if not_found:
            for time in range(start, end):
                self.booked_slots_dic[time] = True

            return True

        else:
            return False
