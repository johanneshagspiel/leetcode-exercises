import collections
from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_string = s.lower()
        cleaned_string = "".join([char for char in lower_string if char.isalnum()])

        string_dequeu = collections.deque(cleaned_string)

        while string_dequeu:

            if len(string_dequeu) == 1:
                return True

            first_char = string_dequeu.popleft()
            last_char = string_dequeu.pop()

            if first_char != last_char:
                return False

        return True

if __name__ == '__main__':
    solution = Solution()

    s = "a"
    output_1 = solution.isPalindrome(s)
    expected_output = 5
    print(output_1)
