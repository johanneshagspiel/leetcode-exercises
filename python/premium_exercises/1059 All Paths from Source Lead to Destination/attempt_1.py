import collections
from typing import List


class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        self.edge_dic = {}

        for starting_location, end_location in edges:
            if starting_location not in self.edge_dic:
                self.edge_dic[starting_location] = []
            self.edge_dic[starting_location].append(end_location)


        if destination in self.edge_dic:
            return False


        self.seen_set = set()

        self.found = False
        self.error = False

        def move(node):

            reachable_locations = self.edge_dic(node)
            filtered_locations = [location for location in reachable_locations if (node, location) not in self.seen_set]

            if filtered_locations == 0:
                if node == destination:
                    self.found = True
                else:
                    self.error = True

            for location in reachable_locations:
                key = (node, location)

                if key not in self.seen_set:
                    self.seen_set.add(key)
                    move(location)


        if self.error:
            return False
        else:
            return self.found
