class Solution:
    def calculate(self, s: str) -> int:

        current_result = 0
        total_result = 0
        operation = "+"
        num = 0

        for char in s + "+":
            if char.isdigit():
                num = 10*num + int(char)

            elif char in ["+", "-", "/", "*"]:
                if operation == "+":
                    current_result += num
                elif operation == "-":
                    current_result -= num
                elif operation == "/":
                    current_result = int(current_result / num)
                elif operation == "*":
                    current_result *= num

                if char in ["+", "-"]:
                    total_result += current_result
                    current_result = 0

                num = 0
                operation = char

        return total_result

