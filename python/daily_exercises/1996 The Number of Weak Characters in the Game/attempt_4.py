from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:

        properties.sort(key= lambda x: x[1], reverse=True)
        properties.sort(key= lambda x: x[0], reverse=False)

        weak_cards = 0
        n = len(properties)
        max_defense = properties[-1][1]

        for position in range(n-2, -1, -1):
            if properties[position][1] > max_defense:
                max_defense = properties[position][1]
            elif properties[position][1] < max_defense:
                weak_cards += 1

        return weak_cards

