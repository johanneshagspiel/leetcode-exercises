from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:

        left_pointer = 0
        right_pointer = len(s) - 1

        while left_pointer < right_pointer:
            left_char = s[left_pointer]
            right_char = s[right_pointer]

            if left_char != right_char:
                s[left_pointer], s[right_pointer] = s[right_pointer], s[left_pointer]

            left_pointer += 1
            right_pointer -= 1

        print(s)

if __name__ == '__main__':

    solution = Solution()
    s = ["h", "e", "l", "l", "o"]
    solution.reverseString(s)