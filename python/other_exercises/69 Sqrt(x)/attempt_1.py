class Solution:
    def mySqrt(self, x: int) -> int:

        num = x // 2

        while True:
            pot = num * num

            if pot <= x:
                break
            else:
                if pot / 2 > x:
                    num = num // 2
                else:
                    num -= 1

        while True:
            test = num + 1
            prod = test * test

            if prod <= x:
                num = test
            else:
                break

        return num

