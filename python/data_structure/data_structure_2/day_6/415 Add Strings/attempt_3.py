class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        len_1 = len(num1) - 1
        len_2 = len(num2) - 1
        carry = 0

        res = []

        while len_1 >= 0 or len_2 >= 0:

            if len_1 >= 0:
                x1= ord(num1[len_1]) - ord('0')
                len_1 -= 1
            else:
                x1 = 0

            if len_2 >= 0:
                x2 = ord(num2[len_2]) - ord('0')
                len_2 -= 1
            else:
                x2 = 0

            temp = (carry + x1 + x2) % 10
            carry = (carry + x1 + x2) // 10

            res.append(temp)

        if carry > 0:
            res.append(carry)

        return "".join(str(x) for x in res[::-1])
