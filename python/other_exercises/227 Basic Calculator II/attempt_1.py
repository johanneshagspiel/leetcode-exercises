class Solution:
    def calculate(self, s: str) -> int:

        def evaluate(operator, num1, num2):

            if operator == "+":
                return num1 + num2
            elif operator == "-":
                return num1 - num2
            elif operator == "*":
                return num1 * num2
            elif operator == "/":
                return num1 // num2


        operation_list = []

        num_acc = ""

        for char in s:
            if not char.isspace():
                if char.isdigit():
                    num_acc += char
                else:
                    if len(num_acc) > 0:
                        temp_num = int(num_acc)
                        operation_list.append(temp_num)
                        num_acc = ""
                    operation_list.append(char)

        if len(num_acc) > 0:
            temp_num = int(num_acc)
            operation_list.append(temp_num)


        res = []

        num_1 = float("inf")
        operator = None

        for iteration in range(2):

            for element in operation_list:
                if isinstance(element, int):
                    if num_1 != float("inf"):
                        num_1 = evaluate(operator, num_1, element)
                    else:
                        num_1 = element
                else:
                    if iteration == 0:
                        if element == "/" or element == "*":
                            operator = element
                        else:
                            res.append(num_1)
                            res.append(element)

                            num_1 = float("inf")
                    else:
                        if element == "+" or element == "-":
                            operator = element
                        else:
                            res.append(num_1)
                            res.append(element)

                            num_1 = float("inf")

            if num_1 != float("inf"):
                res.append(num_1)

            operation_list = res
            res = []
            num_1 = float("inf")
            operator = None

        return operation_list[0]

