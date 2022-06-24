class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        magazine_dic = {}
        for char in magazine:
            if char in magazine_dic:
                magazine_dic[char] += 1
            else:
                magazine_dic[char] = 1

        for char in ransomNote:
            if char not in magazine_dic:
                return False
            else:
                prev_entry = magazine_dic[char]
                prev_entry -= 1
                if prev_entry == 0:
                    magazine_dic.pop(char)
                else:
                    magazine_dic[char] = prev_entry

        return True


if __name__ == '__main__':
    solution = Solution()
    ransomNote = "aa"
    magazine = "ab"
    output = solution.canConstruct(ransomNote, magazine)
    print(output)