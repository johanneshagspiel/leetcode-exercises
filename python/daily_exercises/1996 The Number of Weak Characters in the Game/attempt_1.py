from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:

        if len(properties) == 0:
            return 0

        properties.sort(key= lambda x: x[1], reverse=True)
        properties.sort(key=lambda x: x[0], reverse=False)

        n = len(properties)
        weak_cards = 0

        max_defense = properties[-1][1]

        for position in range(n-2, -1, -1):
            current_defense = properties[position][1]

            if current_defense > max_defense:
                max_defense = current_defense

            elif current_defense < max_defense:
                weak_cards += 1

        return weak_cards
