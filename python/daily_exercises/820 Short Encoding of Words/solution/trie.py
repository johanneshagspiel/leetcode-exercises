import string
from typing import List

class Trie_Node:

    def __init__(self):
        self.children = {}

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie_Node()

        for word in words:
            reverse_word = word[::-1]
            node = trie
            for i in reverse_word:
                if i not in node.children:
                    node.children[i] = Trie_Node()
                node = node.children[i]

        total_length = 0
        stack = []
        stack.append((trie, 0))

        while stack:
            current_node, str_length = stack.pop()

            if len(current_node.children) == 0:
                total_length += (str_length + 1)
            else:
                for i in string.ascii_lowercase:
                    if i in current_node.children:
                        stack.append((current_node.children[i], str_length + 1))

        return total_length
