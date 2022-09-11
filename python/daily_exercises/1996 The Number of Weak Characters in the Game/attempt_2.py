class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:

        max_attack = 0
        for attack, defense in properties:
            max_attack = max(max_attack, attack)


        defense_list = [0 for _ in range(max_attack + 2)]

        for attack, defense in properties:
            defense_list[attack] = max(defense_list[attack], defense)


        for position in range(max_attack):
            defense_list[position] = max(defense_list[position], defense_list[position+1])


        weak_cards = 0

        for attack, defense in properties:
            defense_one_more_attack = defense_list[attack + 1]

            if defense < defense_one_more_attack:
                weak_cards += 1

        return weak_cards
