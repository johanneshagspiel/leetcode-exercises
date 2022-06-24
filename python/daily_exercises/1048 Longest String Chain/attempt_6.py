import string
from typing import List

class Trie_Node:

    def __init__(self):
        self.children = {}
        self.word = False

class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        root = Trie_Node()

        for word in words:
            node = root
            for i in word:
                if i not in node.children:
                    node.children[i] = Trie_Node()
                node = node.children[i]
            node.word = True


        stack = []
        stack.append((root, 0))

        longest_chain = 0

        while stack:
            node, words_encountered = stack.pop()

            if node.word:
                words_encountered += 1
                longest_chain = max(words_encountered, longest_chain)

            for letter in string.ascii_lowercase:
                if letter in node.children:
                    stack.append((node.children[letter], words_encountered))

        return longest_chain

