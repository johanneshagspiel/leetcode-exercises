class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        carry = 0

        len_1 = len(num1)
        len_2 = len(num1)
        max_len = max(len_1, len_2)

        acc = 0

        for shift in range(max_len):
            it = 1 << shift

            carry_s = carry << shift

            bit1 = num1 & it
            bit2 = num2 & it


            if bit1 and bit2 and carry_s:
                acc += carry_s

            elif bit1 and bit2 and not carry_s:
                carry_s = bit1

            elif bit1 and not bit2 and carry_s:
                carry_s = bit1

            elif bit1 and not bit2 and not carry_s:
                acc += bit1

            elif not bit1 and bit2 and carry_s:
                carry_s = bit1

            elif not bit1 and bit2 and not carry_s:
                acc += bit2


            carry = carry_s >> shift

        return acc