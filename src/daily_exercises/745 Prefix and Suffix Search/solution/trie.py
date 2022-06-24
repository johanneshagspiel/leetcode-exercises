from typing import List
class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = {}

        for weight, word in enumerate(words):
            combined_words = word + "#" + word
            word_len = len(word)

            for start_index in range(word_len):
                node = self.trie
                node["$"] = weight

                for i in combined_words[start_index:]:
                    if i not in node:
                        node[i] = {}
                    node = node[i]
                    node["$"] = weight


    def f(self, prefix: str, suffix: str) -> int:
        search_string = suffix + "#" + prefix
        node = self.trie
        for i in search_string:
            if i not in node:
                return -1
            node = node[i]
        return node["$"]