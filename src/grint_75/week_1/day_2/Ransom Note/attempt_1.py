import math
from typing import List

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        magazine_dic = {}
        for char in magazine:
            if char not in magazine_dic:
                prev_entry = [True]
            else:
                prev_entry = magazine_dic[char]
                prev_entry.append(True)
            magazine_dic[char] = prev_entry

        for char in ransomNote:
            if char in magazine_dic:
                prev_entry = magazine_dic[char]
                prev_entry.pop()
                if len(prev_entry) == 0:
                    magazine_dic.pop(char)
            else:
                return False

        return True



if __name__ == '__main__':
    solution = Solution()

    ransomNote = "a"
    magazine = "b"
    output_1 = solution.canConstruct(ransomNote, magazine)
    expected_output = False
    print(output_1)
