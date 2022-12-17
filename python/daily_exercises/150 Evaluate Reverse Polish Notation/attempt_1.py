class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        def _evaluate(left_value, right_value, operator):
            if operator == "+":
                return left_value + right_value
            elif operator == "-":
                return left_value - right_value
            elif operator == "*":
                return left_value * right_value
            elif operator == "/":
                res = int(left_value / right_value)
                return res

        while len(tokens) > 1:
            not_found = True
            left = 0
            new_token_list = []

            while not_found:
                left_char = str(tokens[left])
                if len(left_char) > 1:
                    test_left = left_char[1:]
                else:
                    test_left = left_char

                middle_char = str(tokens[left + 1])
                if len(middle_char) > 1:
                    test_middle = middle_char[1:]
                else:
                    test_middle = middle_char

                right_char = tokens[left + 2]

                if test_left.isnumeric() and test_middle.isnumeric() and (right_char in ["+", "-", "*", "/"]):
                    result = _evaluate(int(left_char), int(middle_char), right_char)
                    new_token_list.append(result)
                    new_token_list.extend(tokens[left + 3:])
                    not_found = False
                else:
                    new_token_list.append(left_char)
                    left += 1

            tokens = new_token_list

        return int(tokens[0])
