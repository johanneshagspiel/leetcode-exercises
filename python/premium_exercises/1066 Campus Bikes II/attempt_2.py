class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:

        def _assign(left_bikes, cur_worker):
            info = (cur_worker, tuple(left_bikes))  # unique identifier of the call parameters
            if info in self.seen:  # if I have computed the min distance for this paramenters before
                return self.seen[info]
            if cur_worker == len(workers):  # if I already assigned all workers
                return 0
            temp = float('inf')  # start calculating the minimum from this assignment onwards
            for j in range(len(left_bikes)):
                if left_bikes[j] == 0:  # assign all left bikes to the current worker
                    left_bikes[j] = 1
                    wx, wy = workers[cur_worker]
                    bx, by = bikes[j]
                    temp = min(temp, abs(wx - bx) + abs(wy - by) + _assign(left_bikes,
                                                                           cur_worker + 1))  # update my minimum considering the minimum between what I had and the distance of this assignment + the minimum distance for the future assignments
                    left_bikes[j] = 0  # unassign bike (instead of creating new left_bike array for every call)
            self.seen[info] = temp  # memoize
            return temp

        self.seen = dict()  # initialize my memoization structure
        return _assign([0 for _ in range(len(bikes))], 0)  # start with all bikes unassigned and with worker 0
