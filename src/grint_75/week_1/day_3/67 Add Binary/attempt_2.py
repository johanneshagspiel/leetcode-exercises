class Solution:
    def addBinary(self, a: str, b: str) -> str:

        x = int(a, 2)
        y = int(b, 2)

        while y != 0:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry

        answer_bin = bin(answer)[2:]

        return answer_bin

if __name__ == "__main__":
    solution = Solution()

    a = "1"
    b = "111"
    output = solution.addBinary(a, b)
    print(output)
