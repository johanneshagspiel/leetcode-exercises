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

        stack = []

        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                num_right = stack.pop()
                num_left = stack.pop()
                res = _evaluate(num_left, num_right, token)
                stack.append(res)
            else:
                stack.append(int(token))

        return stack.pop()
