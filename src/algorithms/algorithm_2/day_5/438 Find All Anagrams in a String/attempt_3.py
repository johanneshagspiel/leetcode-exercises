class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_count = [0 for letter in range(26)]
        p_count = [0 for letter in range(26)]

        for char in p:
            char_index = ord(char) - 97
            p_count[char_index] += 1

        np = len(p)
        ns = len(s)

        output = []

        for i in range(ns):
            s_char = s[i]
            s_char_index = ord(s_char) - 97

            s_count[s_char_index] += 1

            if i >= np:
                left_char = s[i - np]
                left_char_index = ord(left_char) - 97
                s_count[left_char_index] -= 1

            if s_count == p_count:
                output.append(i - np + 1)

        return output