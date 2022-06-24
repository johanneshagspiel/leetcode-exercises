
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        t_dic = {}

        for char in t:
            if char in t_dic:
                pre_entry = t_dic[char]
                pre_entry.append(True)
            else:
                pre_entry = [True]

            t_dic[char] = pre_entry

        for char in s:
            if char not in t_dic:
                return False
            else:
                pre_entry = t_dic[char]
                pre_entry.pop()
                if len(pre_entry) == 0:
                    t_dic.pop(char)
                else:
                    t_dic[char] = pre_entry

        return True


if __name__ == '__main__':
    solution = Solution()

    input_1 = "anagram"
    t = "nagaram"
    output_1 = solution.isAnagram(input_1, t)
    print(output_1)
