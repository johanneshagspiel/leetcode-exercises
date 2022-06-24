import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_list = list(s)
        s_list.sort()

        t_list = list(t)
        t_list.sort()

        return s_list == t_list

if __name__ == '__main__':
    solution = Solution()
    s = "anagram"
    t = "nagaram"
    output = solution.isAnagram(s, t)
    print(output)