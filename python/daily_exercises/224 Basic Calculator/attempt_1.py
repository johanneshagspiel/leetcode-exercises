
class Solution:
    def calculate(self, s: str) -> int:

        def execute_operation(num_1, num_2, operator):
            if operator == "+":
                result = num_1 + num_2
                return result

            elif operator == "-":
                result = num_1 - num_2
                return result

        stack = []

        cur_num = 0
        cur_op = "+"

        regex_pattern = "([1-9][0-9]*|[)(+-])"
        split_string = re.split(regex_pattern, s)

        for element in split_string:
            if (element.isspace() == False):

                if element in ["+", "-"]:
                    cur_op = element

                elif element == "(":
                    stack.append((cur_num, cur_op))
                    cur_num = 0
                    cur_op = "+"

                elif element == ")":
                    prev_num, prev_op = stack.pop()
                    cur_num = execute_operation(prev_num, cur_num, prev_op)

                elif element.isdigit():
                    cur_num = cur_num
                    cur_num = execute_operation(cur_num, int(element), cur_op)


        while stack:
            cur_num = execute_operation(cur_num, prev_num, prev_op)

        return cur_num