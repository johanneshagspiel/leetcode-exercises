class Solution:
    def addBinary(self, a: str, b: str) -> str:

        max_length = max(len(a), len(b))
        a = a.zfill(max_length)
        b = b.zfill(max_length)

        first_number_list = list(a)
        second_number_list = list(b)

        result_list = []
        carry = "0"

        for position in range(max_length - 1, -1, -1):
            top_value = first_number_list[position]
            bottom_value = second_number_list[position]

            if top_value == "1":
                if bottom_value == "1":
                    if carry == "1":
                        result_list.insert(0, "1")
                        carry = "1"
                    else:
                        result_list.insert(0, "0")
                        carry = "1"
                else:
                    if carry == "1":
                        result_list.insert(0, "0")
                        carry = "1"
                    else:
                        result_list.insert(0, "1")
                        carry = "0"
            else:
                if bottom_value == "1":
                    if carry == "1":
                        result_list.insert(0, "0")
                        carry = "1"
                    else:
                        result_list.insert(0, "1")
                        carry = "0"
                else:
                    if carry == "1":
                        result_list.insert(0, "1")
                        carry = "0"
                    else:
                        result_list.insert(0, "0")
                        carry = "0"

        if carry == "1":
            result_list.insert(0, "1")

        result = "".join(result_list)
        return result





if __name__ == "__main__":
    solution = Solution()

    a = "1"
    b = "111"
    output = solution.addBinary(a, b)
    print(output)
