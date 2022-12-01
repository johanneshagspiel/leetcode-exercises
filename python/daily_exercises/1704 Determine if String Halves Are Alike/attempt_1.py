class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        vowel_set = {"a", "e", "i", "o", "u"}

        first_count = 0
        second_count = 0

        for index in range(0, (len(s) // 2), 1):
            lower_char = s[index].lower()
            if lower_char in vowel_set:
                first_count += 1

        for index in range((len(s) // 2), len(s), 1):
            lower_char = s[index].lower()
            if lower_char in vowel_set:
                second_count += 1

        return first_count == second_count
