class Solution:
    def isValid(self, s: str) -> bool:

        open_bracket_set = {"{", "[", "("}
        closed_bracket_set = {"}", "]", ")"}

        correspondence_dic = {"}" : "{", ")" : "(", "]" : "["}

        stack = []

        for i in range(len(s)):
            cur_char = s[i]

            if cur_char in open_bracket_set:
                stack.append(cur_char)
            elif cur_char in closed_bracket_set:

                if len(stack) == 0:
                    return False

                cur_top = stack.pop()
                correspondence_top = correspondence_dic[cur_char]

                if cur_top != correspondence_top:
                    return False

            else:
                return False

        return len(stack) == 0
