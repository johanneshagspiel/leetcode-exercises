class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        max_travel_cost = float("inf")
        max_day = days[-1]
        day_set = set([day for day in days])

        def determine_next_travelling_day(day):
            nonlocal day_set

            if day > max_day:
                return max_day + 1
            else:
                while True:
                    if day in day_set:
                        return day
                    else:
                        day += 1

        def rec_travelling(day, current_cost):
            nonlocal max_travel_cost
            nonlocal max_day

            if day > max_day:
                max_travel_cost = min(max_travel_cost, current_cost)
            else:

                next_day_1 = determine_next_travelling_day(day + 1)
                current_cost_day_1 = current_cost + costs[0]
                rec_travelling(next_day_1, current_cost_day_1)

                next_day_7 = determine_next_travelling_day(day + 7)
                current_cost_day_7 = current_cost + costs[1]
                rec_travelling(next_day_7, current_cost_day_7)

                next_day_30 = determine_next_travelling_day(day + 30)
                current_cost_day_30 = current_cost + costs[2]
                rec_travelling(next_day_30, current_cost_day_30)

        rec_travelling(days[0], 0)
        return max_travel_cost
