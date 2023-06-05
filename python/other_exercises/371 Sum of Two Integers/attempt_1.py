class Solution:
    def getSum(self, a: int, b: int) -> int:

        carry = 0
        acc = 0

        check = 1
        iteration = 0

        while check <= a or check <= b:

            check = check << 1
            carry = carry << 1

            bit = 1 << iteration

            a_bit = a & bit
            b_bit = b & bit

            if b_bit > 0 and a_bit > 0:
                if carry == 0:
                    carry = bit
                else:
                    acc += carry

            elif a_bit == 0 and b_bit == 0:
                if carry > 0:
                    acc += carry
                    carry = 0

            elif a_bit > 0 and b_bit == 0:
                if carry == 0:
                    acc += a_bit

            elif a_bit == 0 and b_bit > 0:
                if carry == 0:
                    acc += b_bit

            iteration += 1

        carry = carry << 1
        acc += carry

        return acc
