class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen_char_dic = {}
        duplicate_set = set()

        for index, char in enumerate(s):
            if char not in seen_char_dic:
                seen_char_dic[char] = (index)
            else:
                duplicate_set.add(char)

        for index, char in enumerate(s):
            if char not in duplicate_set:
                return index

        return -1

if __name__ == '__main__':
    solution = Solution()
    s = "leetcode"
    output = solution.firstUniqChar(s)
    print(output)