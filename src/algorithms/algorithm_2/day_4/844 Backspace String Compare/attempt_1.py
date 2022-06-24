class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        first_pointer = len(s) - 1
        second_pointer = len(t) - 1

        while first_pointer >= 0 and second_pointer >= 0:

            char_s = s[first_pointer]
            first_delete_count = 0
            if char_s == '#':
                first_delete_count += 1

                while (first_pointer >= 0) and (first_delete_count > 0 or char_s == '#'):
                    first_pointer -= 1
                    char_s = s[first_pointer]
                    if char_s == '#':
                        first_delete_count += 1
                    else:
                        first_delete_count -= 1
                        first_pointer -= 1

            char_t = t[second_pointer]
            second_delete_count = 0
            if char_t == '#':
                second_delete_count += 1

                while (second_pointer >= 0) and (second_delete_count > 0 or char_t == '#'):
                    second_pointer -= 1
                    char_t = t[second_pointer]
                    if char_t == '#':
                        second_delete_count += 1
                    else:
                        second_delete_count -= 1
                        second_pointer -= 1


            if first_delete_count > 0 or second_delete_count > 0:
                return False
            elif (first_pointer == 0) and (second_pointer == 0):
                return True
            elif (first_pointer == 0) or (second_pointer == 0):
                return
            else:

                char_s = s[first_pointer]
                char_t = t[second_pointer]

                if char_s != char_t:
                    return False

            first_pointer -= 1
            second_pointer -= 1

        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.backspaceCompare("ab##", "c#d#"))