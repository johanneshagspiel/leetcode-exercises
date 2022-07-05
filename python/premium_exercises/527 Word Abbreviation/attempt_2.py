from typing import List


class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:

        def abbreviate_word(word, i=0):
            if (len(word) - i) <= 3:
                return word
            else:
                new_word = word[:(i + 1)] + str(len(word) - i - 2) + word[-1]
                return new_word

        N = len(words)
        ans = list(map(abbreviate_word, words))
        prefix_list = [0] * N

        for i in range(N):
            while True:
                duplicates = set()

                for j in range(i + 1, N):
                    if ans[i] == ans[j]:
                        duplicates.add(j)

                if len(duplicates) == 0:
                    break
                else:
                    duplicates.add(i)

                    for duplicate_index in duplicates:
                        prefix_list[duplicate_index] += 1
                        ans[duplicate_index] = abbreviate_word(words[duplicate_index], prefix_list[duplicate_index])

        return ans
