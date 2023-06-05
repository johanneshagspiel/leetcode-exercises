class Solution:
    def calculate(self, s: str) -> int:

        num = 0
        current_res = 0
        res = 0
        operation = "+"

        for char in s + "+":

            if char.isdigit():
                num = 10*num + int(char)

            if char in ("+", "-", "*", "/"):

                if operation == "*":
                    current_res *= num

                elif operation == "/":
                    current_res = int(current_res / num)

                elif operation == "+":
                    current_res += num

                elif operation == "-":
                    current_res -= num

                if char in ("+", "-"):
                    res += current_res
                    current_res = 0

                operation = char
                num = 0

        return res
