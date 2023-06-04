import collections


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        graph = collections.defaultdict(list)

        for employee_id, manager_id in enumerate(manager):
            graph[manager_id].append(employee_id)

        max_inform_time = 0
        queue = []
        queue.append((headID, 0))

        while queue:
            manager_id, current_inform_time = queue.pop()
            max_inform_time = max(max_inform_time, current_inform_time)
            manager_inform_time = informTime[manager_id]

            if manager_id in graph:
                employees = graph.pop(manager_id)
                for employee in employees:
                    queue.append((employee, current_inform_time + manager_inform_time))

        return max_inform_time
