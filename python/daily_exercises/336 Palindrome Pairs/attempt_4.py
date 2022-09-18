import collections
from typing import List

class TierNode:

    def __init__(self):
        self.next = collections.defaultdict(TierNode)
        self.word_ending = -1
        self.palindromic_list = []

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        tier = TierNode()

        for index, word in enumerate(words):
            word = word[::-1]

            current_level = tier
            for j, char in enumerate(word):
                if word[j:] == word[j:][::-1]:
                    current_level.palindromic_list.append(index)
                current_level = current_level.next[char]
            current_level.word_ending = index

        solution = []

        for index, word in enumerate(words):

            current_level = tier
            for j, char in enumerate(word):
                if current_level.word_ending != -1:
                    if word[j:] == word[j:][::-1]:
                        solution.append([index, current_level.word_ending])

                if not char in current_level.next:
                    break
                current_level = current_level.next[char]

            else:
                if current_level.word_ending != -1 and current_level.word_ending != index:
                    solution.append([index, current_level.word_ending])

                for j in current_level.palindromic_list:
                    solution.append([index, j])

        return solution
