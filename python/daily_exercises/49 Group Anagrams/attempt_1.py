class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        counter_dic = collections.defaultdict(list)

        for word in strs:
            counter = [0 for _ in range(26)]

            for char in word:
                word_index = ord(char) - ord('a')
                counter[word_index] += 1

            counter_key = "-".join([str(x) for x in counter])

            counter_dic[counter_key].append(word)

        return counter_dic.values()
