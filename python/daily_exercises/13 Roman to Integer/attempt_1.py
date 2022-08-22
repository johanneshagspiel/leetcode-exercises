class Solution:
    def romanToInt(self, s: str) -> int:

        conversion_dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        index_dic = {"I": 0, "V": 1, "X": 2, "L": 3, "C": 4, "D": 5, "M": 6}

        acc_val = 0
        cur_in = -1

        res = 0

        for letter in s:
            letter_in = index_dic[letter]
            letter_val = conversion_dic[letter]

            if cur_in == -1:
                cur_in = letter_in
                acc_val = letter_val

            else:
                if cur_in == letter_in:
                    acc_val += letter_val

                elif cur_in > letter_in:
                    res += acc_val
                    cur_in = letter_in
                    acc_val = letter_val

                else:
                    temp = letter_val - acc_val
                    res += temp
                    acc_val = 0
                    cur_in = -1

        if cur_in != -1:
            res += acc_val

        return res


