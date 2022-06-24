from typing import List

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        s_list = list(s)
        t_list = list(t)

        s_length = len(s_list)
        t_length = len(t_list)

        max_length = max(s_length, t_length)

        word_list_s = []
        wort_list_t = []

        for index in range(max_length):

            if index < s_length:
                s_char = s_list[index]
                if s_char == "#":
                    word_list_s = word_list_s[:-1]
                else:
                    word_list_s.append(s_char)

            if index < t_length:
                t_char = t_list[index]
                if t_char == "#":
                    wort_list_t = wort_list_t[:-1]
                else:
                    wort_list_t.append(t_char)

        return "".join(word_list_s) == "".join(wort_list_t)


if __name__ == '__main__':
    solution = Solution()
    s = "a#c"
    t = "b"
    output = solution.backspaceCompare(s, t)
    print(output)