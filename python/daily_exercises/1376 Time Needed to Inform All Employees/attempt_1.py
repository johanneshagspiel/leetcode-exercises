import collections


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        graph = collections.defaultdict(list)

        for employeeId, managerId in enumerate(manager):
            if managerId != -1:
                graph[managerId].append(employeeId)

        queue = collections.deque()
        queue.append((headID, 0))

        maxInformTime = 0

        while queue:

            queue_len = len(queue)
            for _ in range(queue_len):

                managerId, current_inform_time = queue.popleft()
                maxInformTime = max(maxInformTime, current_inform_time)

                manager_inform_time = informTime[managerId]
                if managerId in graph:
                    subordinates = graph.pop(managerId)
                    for subordinateId in subordinates:
                        queue.append((subordinateId, current_inform_time + manager_inform_time))

        return maxInformTime
