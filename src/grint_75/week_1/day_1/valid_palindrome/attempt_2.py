import collections
from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned_list = list(filter(lambda x: x.isalnum(), s))
        lowered_list = list(map(lambda x: x.lower(), cleaned_list))

        reversed_list = lowered_list[::-1]

        return lowered_list == reversed_list

if __name__ == '__main__':
    solution = Solution()

    s = "A man, a plan, a canal: Panama"
    output_1 = solution.isPalindrome(s)
    expected_output = 5
    print(output_1)
