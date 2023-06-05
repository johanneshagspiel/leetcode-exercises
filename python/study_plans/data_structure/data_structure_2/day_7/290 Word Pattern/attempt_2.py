class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        dic = {}

        string_list = s.split(" ")

        len_p = len(pattern)
        len_s = len(string_list)

        if len_p != len_s:
            return False

        for i in range(len_p):
            char_word = "word_" + string_list[i]
            char_key = "char_" + pattern[i]

            if char_word not in dic:
                dic[char_word] = i

            if char_key not in dic:
                dic[char_key] = i

            if dic[char_key] != dic[char_word]:
                return False

        return True
