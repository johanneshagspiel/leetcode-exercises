
class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        string_dic = {'{' : '}', '[' : ']', '(' : ')'}
        stack = []

        for char in s:
            if char in string_dic:
                stack.append(char)
            else:
                if len(stack) == 0 or string_dic[stack.pop()] != char:
                    return False

        return len(stack) == 0


if __name__ == '__main__':
    solution = Solution()

    input_1 = "([)]"
    output_1 = solution.isValid(input_1)
    print(output_1)
