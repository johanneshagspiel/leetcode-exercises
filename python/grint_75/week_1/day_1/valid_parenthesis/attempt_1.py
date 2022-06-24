
class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        string_list = list(s)

        open_parenthesis_list = []

        for char in string_list:
            if char == '{' or char == '[' or char == '(':
                open_parenthesis_list.append(char)

            elif char == '}' or char == ']' or char == ')':
                if len(open_parenthesis_list) == 0:
                    return False
                else:
                    first_open_char = open_parenthesis_list.pop()

                    if not((first_open_char == '{' and char == '}') or  (first_open_char == '(' and char == ')') or (first_open_char == '[' and char == ']')):
                        return False

        if len(open_parenthesis_list) > 0:
            return False
        else:
            return True


if __name__ == '__main__':
    solution = Solution()

    input_1 = "([)]"
    output_1 = solution.isValid(input_1)
    print(output_1)
