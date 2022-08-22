class Solution:
    def firstUniqChar(self, s: str) -> int:

        index_dic = {}
        double = set()

        for index, char in enumerate(s):
            if char not in double:
                if char in index_dic:
                    index_dic.pop(char)
                    double.add(char)
                else:
                    index_dic[char] = index

        min_index = float("inf")

        for index in index_dic.values():
            if index < min_index:
                min_index = index

        return min_index if min_index != float("inf") else -1

