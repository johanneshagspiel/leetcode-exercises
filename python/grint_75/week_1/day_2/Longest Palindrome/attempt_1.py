class Solution:
    def longestPalindrome(self, s: str) -> int:

        char_dic = {}
        total_length = 0

        for char in s:
            if char not in char_dic:
                char_dic[char] = 1
            else:
                prev_entry = char_dic[char]

                if prev_entry + 1 == 2:
                    total_length += 2
                    char_dic.pop(char)
                else:
                    char_dic[char] = 1

        if len(char_dic) > 0:
            return total_length + 1
        else:
            return total_length

if __name__ == '__main__':
    # test = [1, 1, 1, 2]
    # print(json.dumps(list(itertools.product(test, repeat=4))))

    solution = Solution()
    input_1 = "abccccdd"
    output = solution.longestPalindrome(input_1)
    print(output)