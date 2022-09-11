from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: x[1], reverse=True)
        properties.sort(key=lambda x: x[0], reverse=False)

        max_defense = properties[-1][1]
        weak_card = 0

        n = len(properties)

        for index in range(n-2, -1, -1):
            defense = properties[index][1]

            if defense > max_defense:
                max_defense = defense
            elif defense < max_defense:
                weak_card += 1

        return weak_card

