class Solution:
    def addStrings(self, num1: str, num2: str) -> str:

        mapping = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 0}
        inv = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 0: "0"}

        len_1 = len(num1) - 1
        len_2 = len(num2) - 1
        max_len = max(len_1, len_2) + 1

        res = []
        carry = 0

        for position in range(max_len-1, -1, -1):
            if position > len_1:
                int_1 = 0
            else:
                letter_1 = num1[position]
                int_1 = mapping[letter_1]

            if position > len_2:
                int_2 = 0
            else:
                letter_2 = num2[position]
                int_2 = mapping[letter_2]

            comb = int_1 + int_2 + carry
            temp = comb % 10

            res.append(temp)

            if comb > 10:
                carry = comb // 10

        res = res[::-1]
        str_res = list(map(res, lambda x: str(x)))
        return "".join(str_res)
