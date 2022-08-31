import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if len(ransomNote) > len(magazine):
            return False

        magazine_counter = collections.Counter(magazine)

        for char in ransomNote:
            if magazine_counter[char] <= 0:
                return False
            else:
                magazine_counter[char] -= 1

        return True
