from typing import List

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        s_list = list(s)
        t_list = list(t)

        s_index = len(s) - 1
        t_index = len(t) - 1

        skip_s = 0
        skip_t = 0

        while (s_index >= 0) or (t_index >= 0):

            while (s_index >= 0):
                char_s = s_list[s_index]
                if char_s == "#":
                    skip_s += 1
                    s_index -= 1
                elif skip_s > 0:
                    skip_s -= 1
                    s_index -= 1
                else:
                    break

            while (t_index >= 0):
                char_t = t_list[t_index]
                if char_t == "#":
                    skip_t += 1
                    t_index -= 1
                elif skip_t > 0:
                    skip_t -= 1
                    t_index -= 1
                else:
                    break

            if ((s_index < 0) and (t_index >= 0)) or ((t_index < 0) and (s_index >= 0)):
                return False
            elif char_s != char_t:
                return False
            else:
                s_index -= 1
                t_index -= 1

        return True

