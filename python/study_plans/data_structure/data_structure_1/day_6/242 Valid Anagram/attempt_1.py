import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_counter = collections.Counter(s)

        for char in t:

            if char not in s_counter:
                return False
            else:
                if s_counter[char] <= 0:
                    return False
                else:
                    s_counter[char] -= 1

        return True

if __name__ == '__main__':
    solution = Solution()
    s = "anagram"
    t = "nagaram"
    output = solution.isAnagram(s, t)
    print(output)