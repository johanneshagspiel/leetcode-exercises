class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        first_pointer = len(s) - 1
        second_pointer = len(t) - 1

        while first_pointer >= 0 and second_pointer >= 0:

            char_s = s[first_pointer]
            s_full_delete = False
            if char_s == "#":
                delete_count_s = 1

                while delete_count_s > 0:
                    first_pointer -= 1

                    if first_pointer < 0:
                        s_full_delete = True
                        break
                    else:
                        next_char = s[first_pointer]
                        if next_char == '#':
                            delete_count_s += 1
                        else:
                            first_pointer -= 1
                            if s[first_pointer] != '#':
                                delete_count_s -= 1
            char_s = s[first_pointer]


            char_t = t[second_pointer]
            t_full_delete = False

            while char_t == '#':
                delete_count_t = 1

                while delete_count_t > 0:
                    second_pointer -= 1

                    if second_pointer < 0:
                        t_full_delete = True
                        break
                    else:
                        next_char_t = t[second_pointer]
                        if next_char_t == '#':
                            delete_count_t += 1
                        else:
                            delete_count_t -= 1
                            second_pointer -= 1
                char_t = t[second_pointer]

            if s_full_delete and t_full_delete:
                return True

            if char_s != char_t:
                return False

            first_pointer -= 1
            second_pointer -= 1

        return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.backspaceCompare("gtc#uz#", "gtcm##uz#"))