class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:

        max_attack = 0

        for attack, defense in properties:
            max_attack = max(max_attack, attack)

        max_defense_array = [0 for _ in range(max_attack + 2)]

        for attack, defense in properties:
            max_defense_array[attack] = max(max_defense_array[attack], defense)

        for position in range(max_attack-1):
            max_defense_array[position] = max(max_defense_array[position], max_defense_array[position+1])

        weak_cards = 0

        for attack, defense in properties:
            defense_one_more_attack = max_defense_array[attack + 1]

            if defense < defense_one_more_attack:
                weak_cards += 1

        return weak_cards