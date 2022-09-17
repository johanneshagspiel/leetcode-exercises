import collections
from typing import List


class TrieNode():

    def __init__(self):
        self.next = collections.defaultdict(TrieNode)
        self.palindrome_suffix = []
        self.word_ending = -1


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        trie = TrieNode()

        for index, word in enumerate(words):
            word = word[::-1]
            current_level = trie

            for j, char in enumerate(word):
                if word[j:] == word[j:][::-1]:
                    current_level.palindrome_suffix.append(index)
                current_level = current_level.next[char]

            current_level.word_ending = index

        solutions = []
        for index, word in enumerate(words):
            current_level = trie

            for j, char in enumerate(word):
                if current_level.word_ending != -1:
                    if word[j:] == word[j:][::-1]:
                        solutions.append([index, current_level.word_ending])
                if char not in current_level.next:
                    break
                current_level = current_level.next[char]

            else:
                if current_level.word_ending != -1 and current_level.word_ending != index:
                    solutions.append((index, current_level.word_ending))

                for j in current_level.palindrome_suffix:
                    solutions.append((index, j))

        return solutions
