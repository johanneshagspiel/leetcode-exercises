from typing import List

class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        words.sort(key=lambda x: len(x), reverse=True)

        word_dic = {word: True for word in words}

        def rec_check(current_word):

            max_chain_length = 1

            for index in range(len(current_word)):
                check_word = current_word[:index] + current_word[(index + 1):]
                if check_word in word_dic:
                    chain_length = 1 + rec_check(check_word)
                    max_chain_length = max(max_chain_length, chain_length)

            return max_chain_length

        longest_chain = 1

        for word in words:
            current_chain = rec_check(word)
            longest_chain = max(longest_chain, current_chain)

        return longest_chain

