from typing import List
class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        word_universe = set()
        length_dic = {}

        for word in words:
            word_universe.add(word)

        longest_chain = 1

        for word in words:
            chain_length = self.dfs(word, word_universe, length_dic)
            longest_chain = max(chain_length, longest_chain)

        return longest_chain


    def dfs(self, word, word_universe, length_dic):

        if word in length_dic:
            return length_dic[word]
        else:
            longest_chain = 1

            for index in range(len(word)):
                temp_word = word
                temp_word = temp_word[:index] + temp_word[(index + 1):]
                if temp_word in word_universe:
                    current_length = 1 + self.dfs(temp_word, word_universe, length_dic)
                    longest_chain = max(longest_chain, current_length)

            length_dic[word] = longest_chain

            return longest_chain