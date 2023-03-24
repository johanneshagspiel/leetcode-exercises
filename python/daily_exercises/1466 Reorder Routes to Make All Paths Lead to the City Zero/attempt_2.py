class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        possible_move_dic = {}

        for from_location, to_location in connections:

            if from_location not in possible_move_dic:
                possible_move_dic[from_location] = {}
                possible_move_dic[from_location]["to"] = []
                possible_move_dic[from_location]["from"] = []
            possible_move_dic[from_location]["to"].append(to_location)

            if to_location not in possible_move_dic:
                possible_move_dic[to_location] = {}
                possible_move_dic[to_location]["to"] = []
                possible_move_dic[to_location]["from"] = []
            possible_move_dic[to_location]["from"].append(from_location)


        reachable_locations = []
        reachable_locations.append(0)

        visited_locations = set()
        reorders = 0

        while possible_move_dic:

            while reachable_locations:
                reachable_location = reachable_locations.pop()
                visited_locations.add(reachable_location)

                to_from_dic = possible_move_dic.pop(reachable_location)

                to_list = to_from_dic["to"]
                for to_location in to_list:
                    if to_location not in visited_locations:
                        reorders += 1
                        reachable_locations.append(to_location)

                from_list = to_from_dic["from"]
                for from_location in from_list:
                    if from_location not in visited_locations:
                        reachable_locations.append(from_location)

        return reorders
