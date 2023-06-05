class Solution:
    def calculate(self, s: str) -> int:


        cur_num = ""
        result = 0
        last_num = 0

        for element in s:

            if not element.isspace():

                if element.isnumeric():
                    cur_num += element

                else:

                    cur_num = int(cur_num)

                    if element == "+":
                        result += last_num

                    elif element == "-":
                        result -= last_num

                    elif element == "*":
                        last_num = last_num * cur_num

                    elif element == "/":
                        last_num = last_num / cur_num

                    cur_num = ""

        return result
