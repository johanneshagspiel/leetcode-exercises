import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        char_array = [0]*26

        for index in range(len(s)):
            char_array[ord(s[index]) - 97] += 1

        for index in range(len(t)):
            t_char = t[index]

            entry = char_array[ord(t_char) - 97]
            entry -= 1
            if entry < 0:
                return False
            else:
                char_array[ord(t_char) - 97] = entry

        return True



if __name__ == '__main__':
    solution = Solution()
    s = "anagram"
    t = "nagaram"
    output = solution.isAnagram(s, t)
    print(output)