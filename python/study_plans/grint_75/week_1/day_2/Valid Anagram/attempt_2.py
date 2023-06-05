
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        length = len(s)
        letter_list = [0]*26

        for number in range(0, length):
            letter_list[ord(s[number]) - ord('a')] += 1
            letter_list[ord(t[number]) - ord('a')] -= 1

        for zero in letter_list:
            if zero != 0:
                return False

        return True


if __name__ == '__main__':
    solution = Solution()

    input_1 = "anagram"
    t = "nagaram"
    output_1 = solution.isAnagram(input_1, t)
    print(output_1)
