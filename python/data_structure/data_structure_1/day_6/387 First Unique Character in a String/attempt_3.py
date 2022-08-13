class Solution:
    def firstUniqChar(self, s: str) -> int:

        fixed_array = [0]*26

        for char in s:
            char_index = ord(char) - 97
            fixed_array[char_index] += 1

        for index, char in enumerate(s):
            char_index = ord(char) - 97
            if fixed_array[char_index] == 1:
                return index

        return -1



if __name__ == '__main__':
    solution = Solution()
    s = "z"
    output = solution.firstUniqChar(s)
    print(output)