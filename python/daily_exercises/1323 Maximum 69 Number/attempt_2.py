class Solution:
    def maximum69Number(self, num: int) -> int:

        divisions = 0
        keep_going = True
        modified_num = num
        max_six = -1

        while keep_going:
            last_digit = modified_num % 10
            divisible_six = last_digit % 6 == 0

            if divisible_six:
                max_six = divisions

            divisions += 1

            if modified_num < 10:
                keep_going = False
            else:
                modified_num = modified_num // 10

        if max_six != -1:
            res = num + (3 * (pow(10, max_six)))
            return res
        else:
            return num
