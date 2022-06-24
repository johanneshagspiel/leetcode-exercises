class Solution:
    def isPalindrome(self, s: str) -> bool:

        cleaned_s = [char.lower() for char in s if char.isalnum()]

        left_pointer = 0
        right_pointer = len(cleaned_s) - 1

        while left_pointer < right_pointer:
            char_left = cleaned_s[left_pointer]
            char_right = cleaned_s[right_pointer]

            if char_left != char_right:
                return False
            else:
                left_pointer += 1
                right_pointer -= 1

        return True
