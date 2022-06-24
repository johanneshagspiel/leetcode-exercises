from typing import List
class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        words.sort(key= lambda x: len(x))
        max_string_chain = 0

        word_dic = {}

        for word in words:
            current_word_length = 1

            for index in range(len(word)):
                temp_word = word
                temp_word = temp_word[:index] + temp_word[(index+1):]

                if temp_word in word_dic:
                    previous_length = word_dic[temp_word] + 1
                    current_word_length = max(current_word_length, previous_length)

            word_dic[word] = current_word_length
            max_string_chain = max(max_string_chain, current_word_length)

        return max_string_chain