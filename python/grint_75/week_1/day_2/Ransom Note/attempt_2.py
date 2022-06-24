import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counter = collections.Counter(magazine)

        for char in ransomNote:
            if char not in magazine_counter:
                return False
            elif magazine_counter[char] <= 0:
                return False
            else:
                magazine_counter[char] -= 1

        return True