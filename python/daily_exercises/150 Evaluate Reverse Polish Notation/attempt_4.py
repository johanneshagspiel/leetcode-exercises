class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operations = {
            "+": lambda a, b: a + b,
            "*": lambda a, b: a * b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(a / b)
        }

        stack = []

        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                num_right = stack.pop()
                num_left = stack.pop()
                operation = operations[token]
                res = operation(num_left, num_right)
                stack.append(res)
            else:
                stack.append(int(token))

        return stack.pop()
