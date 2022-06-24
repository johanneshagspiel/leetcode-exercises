from typing import List
class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        word_dic = {}
        words.sort(key=lambda x: len(x))

        longest_chain = 0

        for word in words:
            current_word_length = 1

            for index in range(len(word)):
                temp_word = word[:index] + word[(index + 1):]

                if temp_word in word_dic:
                    previous_length = word_dic[temp_word]
                    current_word_length = max(current_word_length, previous_length + 1)

            word_dic[word] = current_word_length
            longest_chain = max(longest_chain, current_word_length)

        return longest_chain