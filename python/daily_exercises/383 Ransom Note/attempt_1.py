import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        if len(ransomNote) > len(magazine):
            return False

        letter_arr = [0 for _ in range(26)]

        for char in magazine:
            char_index = ord(char) - ord('a')
            letter_arr[char_index] += 1

        for char in ransomNote:
            char_index = ord(char) - ord('a')

            if letter_arr[char_index] > 0:
                letter_arr[char_index] -= 1
            else:
                return False

        return True
