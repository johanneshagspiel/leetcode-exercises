class Solution:
    def firstUniqChar(self, s: str) -> int:

        seen_dic = {}

        for char in s:
            if char not in seen_dic:
                seen_dic[char] = 1
            else:
                seen_dic[char] += 1

        for index, char in enumerate(s):
            if seen_dic[char] == 1:
                return index

        return -1

if __name__ == '__main__':
    solution = Solution()
    s = "leetcode"
    output = solution.firstUniqChar(s)
    print(output)