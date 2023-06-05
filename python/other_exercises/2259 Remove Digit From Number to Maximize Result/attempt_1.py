class Solution:
    def removeDigit(self, number: str, digit: str) -> str:

        if len(number) == 1:
            if number[0] == digit:
                return ""
            else:
                return number

        prev_smallest = float("inf")
        remove_index = -1

        for index, char in enumerate(number):

            if char == digit:
                if index == 0:
                    compare_int = int(number[1])
                else:
                    compare_int = int(number[index-1])

                if compare_int < prev_smallest:
                    prev_smallest = compare_int
                    remove_index = index

        if remove_index == -1:
            return number

        else:
            return "".join(number[:remove_index] + number[(remove_index+1):])


