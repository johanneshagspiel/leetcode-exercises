class Solution:
    def calculate(self, s: str) -> int:

        stack = []


        num = 0
        operation = "+"
        N = len(s)

        for index, char in enumerate(s):

            if char.isdigit():
                num = 10*num + int(char)

            if (not char.isdigit() and not char.isspace() ) or (index == N- 1):

                if operation == "+":
                    stack.append(num)
                elif operation == "-":
                    stack.append(-num)
                elif operation == "*":
                    num2 = stack.pop()
                    res = num*num2
                    stack.append(res)
                elif operation == "/":
                    num2 = stack.pop()
                    res = int(num2 / num)
                    stack.append(res)

                num = 0
                operation = char

        res = 0

        while stack:
            num = stack.pop()
            res += num

        return res
