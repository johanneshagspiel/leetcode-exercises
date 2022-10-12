class Solution:
    def breakPalindrome(self, palindrome: str) -> str:

        n = len(palindrome)

        if n <= 1:
            return ""

        is_odd = n % 2 == 1
        mid_way_index = n // 2

        changed = False

        new_res = ""

        for i in range(n):
            char_num = ord(palindrome[i]) - ord('a')

            if not changed:
                if char_num > 0 and (i != n - 1):
                    if not (is_odd and (i == mid_way_index)):
                        changed = True
                        new_res += 'a'
                        
                    else:
                        new_res += palindrome[i]

                elif char_num == 0 and (i == n - 1):
                    changed = True
                    new_res += 'b'

                else:
                    new_res += palindrome[i]
            else:
                new_res += palindrome[i]

        if changed:
            return new_res
        else:
            return ""
