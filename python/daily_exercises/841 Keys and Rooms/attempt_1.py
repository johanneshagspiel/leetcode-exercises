class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        key_set = set()
        seen_rooms = set()

        for key in rooms[0]:
            key_set.add(key)
        seen_rooms.add(0)

        while key_set:

            if len(seen_rooms) == len(rooms):
                return True

            else:

                new_key_set = set()

                for key in key_set:
                    if key not in seen_rooms:
                        seen_rooms.add(key)
                        new_room = rooms[key]

                        for new_key in new_room:
                            new_key_set.add(new_key)

                key_set = new_key_set
                if len(seen_rooms) == len(rooms):
                    return True

        return False
