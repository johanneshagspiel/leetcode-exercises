class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

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

        def rec_travelling(day, mem_dic):
            nonlocal max_day

            if day > max_day:
                return 0
            if day in mem_dic:
                return mem_dic[day]
            else:
                next_day_1 = determine_next_travelling_day(day + 1)
                current_cost_day_1 = costs[0] + rec_travelling(next_day_1, mem_dic)

                next_day_7 = determine_next_travelling_day(day + 7)
                current_cost_day_7 = costs[1] + rec_travelling(next_day_7, mem_dic)

                next_day_30 = determine_next_travelling_day(day + 30)
                current_cost_day_30 = costs[2] + rec_travelling(next_day_30, mem_dic)

                mem_dic[day] = min(current_cost_day_1, current_cost_day_7, current_cost_day_30)
                return mem_dic[day]

        return rec_travelling(days[0], {})
