class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        dif_list = []

        for i in range(len(rocks)):
            dif = capacity[i] - rocks[i]
            dif_list.append(dif)

        dif_list.sort()

        max_full = 0

        for dif in dif_list:
            if dif <= additionalRocks:
                additionalRocks -= dif
                max_full += 1

        return max_full

